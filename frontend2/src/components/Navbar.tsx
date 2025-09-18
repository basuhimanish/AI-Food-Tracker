"use client"

import { useState, useEffect } from "react"
import { Link, useLocation, useNavigate } from "react-router-dom"
import { useAuth } from "../contexts/AuthContext"
import { apiService } from "../services/api"
import {
  HomeIcon,
  CubeIcon,
  CameraIcon,
  HeartIcon,
  BookOpenIcon,
  ShoppingCartIcon,
  UserIcon,
  Bars3Icon,
  XMarkIcon,
} from "@heroicons/react/24/outline"

export default function Navbar() {
  const { user, logout } = useAuth()
  const location = useLocation()
  const navigate = useNavigate()
  const [isMenuOpen, setIsMenuOpen] = useState(false)
  const [userPoints, setUserPoints] = useState(0)

  useEffect(() => {
    if (user?.userid) {
      fetchUserPoints()
    }
  }, [user?.userid])

  const fetchUserPoints = async () => {
    try {
      const response = await apiService.getUserPoints(user!.userid)
      if (response.data.status) {
        setUserPoints(response.data.points)
      }
    } catch (error) {
      console.error("Error fetching user points:", error)
    }
  }

  const handleLogout = () => {
    logout()
    navigate("/login")
  }

  const navItems = [
    { name: "Dashboard", path: "/dashboard", icon: HomeIcon },
    { name: "Inventory", path: "/inventory", icon: CubeIcon },
    { name: "Scan Item", path: "/scan", icon: CameraIcon },
    { name: "Donate", path: "/donate", icon: HeartIcon },
    { name: "Recipes", path: "/recipes", icon: BookOpenIcon },
    { name: "Groceries", path: "/groceries", icon: ShoppingCartIcon },
  ]

  return (
    <nav className="bg-white shadow-lg fixed top-0 left-0 right-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          {/* Logo */}
          <div className="flex items-center">
            <Link to="/dashboard" className="flex items-center space-x-2">
              <div className="w-8 h-8 bg-green-500 rounded-lg flex items-center justify-center">
                <span className="text-white font-bold text-lg">🍎</span>
              </div>
              <span className="text-xl font-bold text-gray-800">FoodTracker</span>
            </Link>
          </div>

          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center space-x-8">
            {navItems.map((item) => {
              const Icon = item.icon
              return (
                <Link
                  key={item.name}
                  to={item.path}
                  className={`flex items-center space-x-1 px-3 py-2 rounded-md text-sm font-medium transition-colors ${
                    location.pathname === item.path
                      ? "text-green-600 bg-green-50"
                      : "text-gray-600 hover:text-green-600 hover:bg-green-50"
                  }`}
                >
                  <Icon className="w-4 h-4" />
                  <span>{item.name}</span>
                </Link>
              )
            })}
          </div>

          {/* User Menu */}
          <div className="hidden md:flex items-center space-x-4">
            {/* Points Display */}
            <div className="flex items-center space-x-2 bg-yellow-100 px-3 py-2 rounded-lg">
              <span className="text-yellow-600 text-lg">🪙</span>
              <span className="text-sm font-semibold text-yellow-800">{userPoints} points</span>
            </div>
            <div className="flex items-center space-x-2">
              <UserIcon className="w-5 h-5 text-gray-600" />
              <span className="text-sm text-gray-700">Hi, {user?.username}</span>
            </div>
            <button
              onClick={handleLogout}
              className="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-md text-sm font-medium transition-colors"
            >
              Logout
            </button>
          </div>

          {/* Mobile menu button */}
          <div className="md:hidden flex items-center">
            <button
              onClick={() => setIsMenuOpen(!isMenuOpen)}
              className="text-gray-600 hover:text-gray-900 focus:outline-none focus:text-gray-900"
            >
              {isMenuOpen ? <XMarkIcon className="w-6 h-6" /> : <Bars3Icon className="w-6 h-6" />}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Navigation */}
      {isMenuOpen && (
        <div className="md:hidden">
          <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3 bg-white border-t">
            {navItems.map((item) => {
              const Icon = item.icon
              return (
                <Link
                  key={item.name}
                  to={item.path}
                  onClick={() => setIsMenuOpen(false)}
                  className={`flex items-center space-x-2 px-3 py-2 rounded-md text-base font-medium ${
                    location.pathname === item.path
                      ? "text-green-600 bg-green-50"
                      : "text-gray-600 hover:text-green-600 hover:bg-green-50"
                  }`}
                >
                  <Icon className="w-5 h-5" />
                  <span>{item.name}</span>
                </Link>
              )
            })}
            <div className="border-t pt-4">
              {/* Points Display for Mobile */}
              <div className="flex items-center space-x-2 px-3 py-2 bg-yellow-100 rounded-lg mx-3 mb-2">
                <span className="text-yellow-600 text-lg">🪙</span>
                <span className="text-sm font-semibold text-yellow-800">{userPoints} points</span>
              </div>
              <div className="flex items-center space-x-2 px-3 py-2">
                <UserIcon className="w-5 h-5 text-gray-600" />
                <span className="text-sm text-gray-700">Hi, {user?.username}</span>
              </div>
              <button
                onClick={handleLogout}
                className="w-full text-left px-3 py-2 text-red-600 hover:bg-red-50 rounded-md font-medium"
              >
                Logout
              </button>
            </div>
          </div>
        </div>
      )}
    </nav>
  )
}
