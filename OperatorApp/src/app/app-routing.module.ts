import { NgModule } from "@angular/core";
import { RouterModule, Routes } from "@angular/router";

const routes: Routes = [
    {
        path: "**",
        redirectTo: "account",
        pathMatch: "full",
    },
    {
        path: "account",
        children: [
            {
                path: "",
                loadChildren: () =>
                    import("./account/account.module").then(
                        m => m.AccountModule
                    ),
            },
        ],
    },
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule],
})
export class AppRoutingModule {}
