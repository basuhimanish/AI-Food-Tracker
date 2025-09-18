import { Link } from "react-router-dom"

export default function Footer() {
  return (
    <footer className="bg-gray-800 text-white">
      <div className="max-w-7xl mx-auto py-8 px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div>
            <div className="flex items-center space-x-2 mb-4">
              <div className="w-8 h-8 bg-green-500 rounded-lg flex items-center justify-center">
                <span className="text-white font-bold text-lg">🍎</span>
              </div>
              <span className="text-xl font-bold">FoodTracker</span>
            </div>
            <p className="text-gray-300 text-sm">Smart food management to reduce waste and save money.</p>
          </div>

          <div>
            <h3 className="text-lg font-semibold mb-4">Quick Links</h3>
            <div className="space-y-2">
              <Link to="/dashboard" className="block text-gray-300 hover:text-white text-sm">
                Dashboard
              </Link>
              <Link to="/inventory" className="block text-gray-300 hover:text-white text-sm">
                My Inventory
              </Link>
              <Link to="/recipes" className="block text-gray-300 hover:text-white text-sm">
                Recipes
              </Link>
            </div>
          </div>

          <div>
            <h3 className="text-lg font-semibold mb-4">Support</h3>
            <div className="space-y-2">
              <a href="#" className="block text-gray-300 hover:text-white text-sm">
                About
              </a>
              <a href="#" className="block text-gray-300 hover:text-white text-sm">
                Privacy Policy
              </a>
              <a href="#" className="block text-gray-300 hover:text-white text-sm">
                Contact
              </a>
            </div>
          </div>
        </div>

        <div className="border-t border-gray-700 mt-8 pt-8 text-center">
          <p className="text-gray-300 text-sm">© 2024 FoodTracker. All rights reserved.</p>
        </div>
      </div>
    </footer>
  )
}
