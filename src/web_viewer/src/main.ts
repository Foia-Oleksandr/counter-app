import {Viewer} from "./Viewer";
import "./style.css";
import type {BoxSpec, SphereSpec} from "3dmol";
import {setupWebChannel} from "./web-chanel-interface";

const CONTAINER_ID = "viewer-container";

function addWireframeBox(viewer: Viewer) {
    console.log("TS: addWireframeBox called");
    const box: BoxSpec = {
        corner: {x: 0, y: 0, z: 0},
        dimensions: {w: 5, h: 5, d: 7},
        color: 'black',
        wireframe: true,
        linewidth: 10
    };
    viewer.addBox(box)
    const sphere: SphereSpec = {center: {x: 0, y: 0, z: 0}, radius: 1.5, color: 'red'};
    viewer.addSphere(sphere);
    viewer.setStyle({stick: {radius: 0.15}, sphere: {radius: 0.28}})
    viewer.render();
}

window.addEventListener("DOMContentLoaded", () => {
    const container = document.getElementById(CONTAINER_ID);
    if (!container) {
        throw new Error(`Container #${CONTAINER_ID} not found`);
    }
    setupWebChannel(container, (viewer) => addWireframeBox(viewer));

    console.log("TS: script loaded");
});