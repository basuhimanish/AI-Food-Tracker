import axios from "axios"

// const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000"
const API_BASE_URL = "http://localhost:8000"

export const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
})

// API functions
export const apiService = {
  // Auth
  login: (email: string, password: string) => api.post("/user/verify", { email, password }),

  signup: (name: string, email: string, password: string) => api.post("/user/add", { name, email, password }),

  // Inventory
  getInventory: (userid: string) => api.post("/user/inventory", {userid}),
  
  // Mark item as consumed/donated/expired
  updateFoodStatus: (inventory_id: number, status: string, notes: string) => 
    api.post("/user/foodstatus", { inventory_id, status, notes }),
  
  // Delete inventory item
  deleteInventoryItem: (inventory_id: number, userid: string) => 
    api.delete(`/user/inventory/${inventory_id}?userid=${userid}`),
  
  // Mark items as donated
  donateItems: (inventory_ids: number[], userid: string) => 
    api.post("/user/donate", { inventory_ids, userid }),
  
  // Get user points
  getUserPoints: (userid: string) => api.get(`/user/points/${userid}`),



  // Scan item
  scanItem: (expiry_date: string, userid: string) => api.post("/item/scan", { expiry_date, userid }),

  // Recipe suggestions
  getRecipeSuggestions: (ingredients: string[]) => api.post("/user/recipe/suggestions", { ingredients }),

  // Verify item by barcode
  verifyItem: (barcode: string) => api.post("/admin/verifyitem", { barcode }),
}
