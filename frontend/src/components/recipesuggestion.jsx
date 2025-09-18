import App from "next/app";

export default function RecipeSuggestion({ userid }) {
  async function retrieve_food_items() {
    return await App.post(userid, "/user/inventory");
  }

  async function suggest_recipes() {
    const inventory = retrieve_food_items();
    const recipe_suggestions = await App.post(inventory, "/user/suggestion");
  }

  return (
    <div>
      <div>
        <button onClick={() => suggest_recipes()}>Suggest Recipes</button>
      </div>
    </div>
  );
}
