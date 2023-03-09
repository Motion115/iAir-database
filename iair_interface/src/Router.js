// Import React Router components
import { BrowserRouter, Routes, Route } from "react-router-dom";

// Import your custom components
import Home from "./App.js"
import Info from "./management.js"

// Create a function component that renders the routes
function Router() {
  return (
    // Wrap your app with BrowserRouter
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/info" element={<Info />} />
      </Routes>
    </BrowserRouter>
  );
}

export default Router;