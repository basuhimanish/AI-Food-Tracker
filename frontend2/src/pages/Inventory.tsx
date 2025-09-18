"use client"

import { useState, useEffect } from "react"
import { useAuth } from "../contexts/AuthContext"
import { apiService } from "../services/api"
import { MagnifyingGlassIcon, FunnelIcon, TrashIcon, ExclamationTriangleIcon } from "@heroicons/react/24/outline"

interface InventoryItem {
  inventory_id: number
  f_id: number
  f_name: string
  brands: string
  quantity: string
  energy: number
  category: string
  expiry_date: string
  imageurl: string
}

export default function Inventory() {
  const { user } = useAuth()
  const [items, setItems] = useState<InventoryItem[]>([])
  const [filteredItems, setFilteredItems] = useState<InventoryItem[]>([])
  const [loading, setLoading] = useState(true)
  const [searchTerm, setSearchTerm] = useState("")
  const [sortBy, setSortBy] = useState("expiry")
  const [filterBy, setFilterBy] = useState("all")

  useEffect(() => {
    fetchInventory()
  }, [])

  useEffect(() => {
    filterAndSortItems()
  }, [items, searchTerm, sortBy, filterBy])

  const fetchInventory = async () => {
    if (!user?.userid) {
      console.log("No user found")
      setLoading(false)
      return
    }

    console.log("Fetching inventory for user:", user.userid)
    try {
      const response = await apiService.getInventory(user.userid)
      console.log("Inventory response:", response)
      if (Array.isArray(response.data)) {
        setItems(response.data)
        console.log("Items set:", response.data)
      } else {
        console.log("Response data is not an array:", response.data)
      }
    } catch (error) {
      console.error("Error fetching inventory:", error)
    } finally {
      setLoading(false)
    }
  }

  const filterAndSortItems = () => {
    let filtered = items.filter(
      (item) =>
        item.f_name.toLowerCase().includes(searchTerm.toLowerCase()) ||
        item.brands.toLowerCase().includes(searchTerm.toLowerCase()),
    )

    // Filter by expiry
    if (filterBy === "expiring") {
      const threeDaysFromNow = new Date()
      threeDaysFromNow.setDate(threeDaysFromNow.getDate() + 3)
      filtered = filtered.filter((item) => new Date(item.expiry_date) <= threeDaysFromNow)
    }

    // Sort items
    filtered.sort((a, b) => {
      switch (sortBy) {
        case "expiry":
          return new Date(a.expiry_date).getTime() - new Date(b.expiry_date).getTime()
        case "name":
          return a.f_name.localeCompare(b.f_name)
        case "category":
          return a.category.localeCompare(b.category)
        default:
          return 0
      }
    })

    setFilteredItems(filtered)
  }

  const isExpiringSoon = (expiryDate: string) => {
    const expiry = new Date(expiryDate)
    const today = new Date()
    const diffTime = expiry.getTime() - today.getTime()
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24))
    return diffDays <= 3
  }

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString("en-US", {
      year: "numeric",
      month: "short",
      day: "numeric",
    })
  }

  const markItemAsConsumed = async (inventoryId: number) => {
    try {
      await apiService.updateFoodStatus(inventoryId, "consumed", "Marked as consumed by user")
      // Refresh the inventory to reflect the change
      await fetchInventory()
    } catch (error) {
      console.error("Error marking item as consumed:", error)
    }
  }

  const deleteItem = async (inventoryId: number) => {
    if (!user?.userid) {
      console.error("No user found")
      return
    }
    
    try {
      const response = await apiService.deleteInventoryItem(inventoryId, user.userid)
      if (response.data.status) {
        // Refresh the inventory to reflect the change
        await fetchInventory()
        console.log("Item deleted successfully")
      } else {
        console.error("Failed to delete item:", response.data.message)
      }
    } catch (error) {
      console.error("Error deleting item:", error)
    }
  }

  if (loading) {
    return (
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="animate-pulse">
          <div className="h-8 bg-gray-200 rounded w-1/4 mb-6"></div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {[...Array(6)].map((_, i) => (
              <div key={i} className="bg-gray-200 h-64 rounded-lg"></div>
            ))}
          </div>
        </div>
      </div>
    )
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">My Inventory</h1>
        <p className="text-gray-600">Manage your food items and track expiry dates</p>
      </div>

      {/* Search and Filters */}
      <div className="bg-white rounded-lg shadow-sm p-6 mb-6">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="relative">
            <MagnifyingGlassIcon className="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
            <input
              type="text"
              placeholder="Search items..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          <div className="relative">
            <FunnelIcon className="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
            <select
              value={filterBy}
              onChange={(e) => setFilterBy(e.target.value)}
              className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 appearance-none"
            >
              <option value="all">All Items</option>
              <option value="expiring">Expiring Soon</option>
            </select>
          </div>

          <select
            value={sortBy}
            onChange={(e) => setSortBy(e.target.value)}
            className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="expiry">Sort by Expiry</option>
            <option value="name">Sort by Name</option>
            <option value="category">Sort by Category</option>
          </select>
        </div>
      </div>

      {/* Items Grid */}
      {filteredItems.length === 0 ? (
        <div className="text-center py-12">
          <div className="text-gray-400 text-lg mb-2">No items found</div>
          <p className="text-gray-600">
            {items.length === 0
              ? "Start by scanning some items to build your inventory"
              : "Try adjusting your search or filters"}
          </p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredItems.map((item) => (
            <div
              key={item.inventory_id}
              className={`bg-white rounded-lg shadow-sm border-2 transition-all hover:shadow-md ${
                isExpiringSoon(item.expiry_date) ? "border-yellow-300 bg-yellow-50" : "border-gray-200"
              }`}
            >
              <div className="p-6">
                {isExpiringSoon(item.expiry_date) && (
                  <div className="flex items-center text-yellow-600 mb-2">
                    <ExclamationTriangleIcon className="h-4 w-4 mr-1" />
                    <span className="text-xs font-medium">Expiring Soon</span>
                  </div>
                )}

                <div className="flex items-start justify-between mb-4">
                  <div className="flex-1">
                    <h3 className="font-semibold text-gray-900 mb-1 line-clamp-2">{item.f_name}</h3>
                    <p className="text-sm text-gray-600">{item.brands}</p>
                  </div>
                  <button onClick={() => deleteItem(item.inventory_id)} className="text-red-500 hover:text-red-700 p-1">
                    <TrashIcon className="h-4 w-4" />
                  </button>
                </div>

                <div className="space-y-2 text-sm">
                  <div className="flex justify-between">
                    <span className="text-gray-600">Quantity:</span>
                    <span className="font-medium">{item.quantity}</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-gray-600">Category:</span>
                    <span className="font-medium capitalize">{item.category}</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-gray-600">Expires:</span>
                    <span
                      className={`font-medium ${
                        isExpiringSoon(item.expiry_date) ? "text-yellow-600" : "text-gray-900"
                      }`}
                    >
                      {formatDate(item.expiry_date)}
                    </span>
                  </div>
                  {item.energy > 0 && (
                    <div className="flex justify-between">
                      <span className="text-gray-600">Energy:</span>
                      <span className="font-medium">{item.energy} kcal/100g</span>
                    </div>
                  )}
                </div>

                <div className="mt-4 pt-4 border-t border-gray-200">
                  <button 
                    onClick={() => markItemAsConsumed(item.inventory_id)}
                    className="w-full bg-green-600 hover:bg-green-700 text-white py-2 px-4 rounded-lg text-sm font-medium transition-colors"
                  >
                    Mark as Consumed
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}
