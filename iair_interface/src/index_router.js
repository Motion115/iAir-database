// Import React Router components
import { BrowserRouter, Routes, Route } from "react-router-dom";

// Import your custom components
import Home from "./App_general_stats.js"
import CityStats from "./App_city_stats.js"
import Professional from "./App_professional.js"
import Manager from "./App_manager.js"

// Create a function component that renders the routes
function Router() {
	return (
		// Wrap your app with BrowserRouter
		<BrowserRouter>
			<Routes>
				<Route path="/" element={<Home />} />
				<Route path="/citystats" element={<CityStats />} />
				<Route path="/professional" element={<Professional />} />
				<Route path="/manager" element={<Manager />} />
			</Routes>
		</BrowserRouter>
	);
}

export default Router;