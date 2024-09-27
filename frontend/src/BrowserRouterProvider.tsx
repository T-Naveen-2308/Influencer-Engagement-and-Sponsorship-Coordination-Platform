import {
    createBrowserRouter,
    RouterProvider,
    Navigate
} from "react-router-dom";
import { useSelector } from "react-redux";

function BrowserRouterProvider() {
    let isAuthenticated;

    const BrowserRouter = createBrowserRouter([{}]);

    return (
        <>
            <RouterProvider router={BrowserRouter} />
        </>
    );
}

export default BrowserRouterProvider;
