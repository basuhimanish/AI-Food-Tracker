"use client"

import { useState } from "react"
import { useAuth } from "../contexts/AuthContext"
import { apiService } from "../services/api"
import { CameraIcon } from "@heroicons/react/24/outline"

export default function Scan() {
  const { user } = useAuth()
  const [expiryDate, setExpiryDate] = useState("")
  const [loading, setLoading] = useState(false)
  const [message, setMessage] = useState("")
  const [scannedProduct, setScannedProduct] = useState<any>(null)

  const scanBarcode = async () => {
    if (!user?.userid || !expiryDate) {
      setMessage("Please select an expiry date first")
      return
    }

    setLoading(true)
    setMessage("Opening camera for barcode scanning...")
    
    try {
      const response = await apiService.scanItem(expiryDate, user.userid)
      if (response.data.message === "success") {
        setMessage("Item added to inventory successfully!")
        // Reset form
        setExpiryDate("")
        setScannedProduct(null)
      } else {
        setMessage("Failed to add item to inventory")
      }
    } catch (error) {
      console.error("Scan error:", error)
      setMessage("Error scanning barcode. Please try again.")
    } finally {
      setLoading(false)
    }
  }

  const resetForm = () => {
    setExpiryDate("")
    setScannedProduct(null)
    setMessage("")
  }

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div className="text-center mb-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">Scan Item</h1>
        <p className="text-gray-600">Scan barcodes to add items to your inventory</p>
      </div>

      <div className="bg-white rounded-xl shadow-lg p-6">
        <div className="text-center">
          <div className="mb-6">
            <CameraIcon className="mx-auto h-24 w-24 text-gray-400" />
          </div>
          
          <div className="mb-6">
            <label htmlFor="expiryDate" className="block text-sm font-medium text-gray-700 mb-2">
              Expiry Date *
            </label>
            <input
              type="date"
              id="expiryDate"
              value={expiryDate}
              onChange={(e) => setExpiryDate(e.target.value)}
              className="w-full max-w-md mx-auto px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              required
            />
          </div>

          <button
            onClick={scanBarcode}
            disabled={loading || !expiryDate}
            className="bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white px-8 py-3 rounded-lg font-medium transition-colors"
          >
            {loading ? "Scanning..." : "Scan Barcode & Add to Inventory"}
          </button>

          {message && (
            <div
              className={`mt-4 p-4 rounded-lg ${
                message.includes("success") ? "bg-green-100 text-green-800" : "bg-red-100 text-red-800"
              }`}
            >
              {message}
            </div>
          )}

          {!loading && (message.includes("success") || message.includes("Failed")) && (
            <button
              onClick={resetForm}
              className="mt-4 px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 transition-colors"
            >
              Scan Another Item
            </button>
          )}
        </div>
      </div>
    </div>
  )
}
