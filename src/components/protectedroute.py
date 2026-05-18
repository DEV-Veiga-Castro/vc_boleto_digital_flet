import flet as ft

@ft.component
def ProtectedRoute():
    outlet = ft.use_route_outlet()

    if not ft.auth.is_authenticated:
        ft.context.page.navigate("/login")
        return ft.Text("Redirecting...")
    
    return outlet