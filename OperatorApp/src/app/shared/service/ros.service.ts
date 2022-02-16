import { Injectable } from "@angular/core";
import * as ROSLIB from "roslib";
import { environment } from "../../../environments/environment";

@Injectable({
    providedIn: "root",
})
export class RosService {
    private ros: ROSLIB.Ros;
    private robotIp = environment.robotIp;
    private robotPort = environment.robotPort;

    constructor() {
        this.ros = new ROSLIB.Ros({});
        this.ros.on("error", function(error: any) {
            console.log(error);
        });
        this.ros.on("connection", function(error: any) {
            console.log("connection");
            console.log(error);
        });
        this.ros.on("close", function(error: any) {
            console.log("close");
            console.log(error);
        });
        this.ros.connect("ws://" + this.robotIp + ":" + this.robotPort);
    }

    public getMessageObservable() {
        var mesageTopicObservable = new ROSLIB.Topic({
            ros: this.ros,
            name: "/camera1_compressed",
            messageType: "sensor_msgs/CompressedImage",
        });

        return mesageTopicObservable;
    }
}
