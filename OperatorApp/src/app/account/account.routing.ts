import { NgModule } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";
import { DashboardComponent } from "./dashboard/dashboard.component";
import { NavComponent } from "./nav/nav.component";

const accountRoutes: Routes = [
    {
        path: "dashboard",
        component: NavComponent,
        children: [
            {
                path: "",
                component: DashboardComponent,
            },
        ],
    },
    {
        path: "**",
        redirectTo: "dashboard",
        pathMatch: "full",
    },
];

@NgModule({
    imports: [RouterModule.forChild(accountRoutes)],
    exports: [RouterModule],
})
export class AccountRoutingModule {}
