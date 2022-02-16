import { Component, OnInit } from "@angular/core";
import { RosService } from "../../shared/service/ros.service";
import { SafeResourceUrl, DomSanitizer } from "@angular/platform-browser";

@Component({
    selector: "app-dashboard",
    templateUrl: "./dashboard.component.html",
    styleUrls: ["./dashboard.component.scss"],
})
export class DashboardComponent implements OnInit {
    dataUrl: SafeResourceUrl = "";

    constructor(
        private rosService: RosService,
        private domSanitizer: DomSanitizer
    ) {}

    ngOnInit(): void {
        this.rosService.getMessageObservable().subscribe((message: any) => {
            this.dataUrl = this.domSanitizer.bypassSecurityTrustResourceUrl(
                "data:image/jpg;base64, " + message.data
            );
        });
    }
}
