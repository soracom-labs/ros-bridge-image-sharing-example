# Operator App

This app will subscribe websocket and show base64 encoded images.

## Prerequisite

- Angular: 12.1.3.
- Nodejs: v14.17.3

## Configure

Edit `robotIp` and `robotPort` in [environment.ts](./src/environments/environment.ts).

```
export const environment = {
    production: false,
    robotIp: "10.198.97.225",
    robotPort: "9090",
};
```

## Run

Execute the following command and open [http://localhost:4200](http://localhost:4200) in your browser.

```
npm install
ng serve
```
