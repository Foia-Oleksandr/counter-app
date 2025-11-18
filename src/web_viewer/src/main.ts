import {Viewer} from "./Viewer";
import "./style.css";
import type {BoxSpec} from "3dmol";

function initViewer() {
    const containerId = "viewer-container";
    const container = document.getElementById(containerId);
    if (!container) {
        throw new Error(`Container #${containerId} not found`);
    }
    // window._viewer =
    return new Viewer(container);
}

function setupWebChannel(viewer: Viewer) {

}

function addWireframeBox(viewer: Viewer) {
    const box: BoxSpec = {
        corner: {x: 0, y: 0, z:0},
        dimensions: {w: 5, h: 5, d: 7},
        color: 'black',
        wireframe: true,
        linewidth: 10
    };
    viewer.addBox(box)
    viewer.setStyle({stick: {radius: 0.15}, sphere: {radius: 0.28}})
    viewer.render();
}

window.addEventListener("DOMContentLoaded", () => {
    const viewer = initViewer();
    setupWebChannel(viewer);
    addWireframeBox(viewer);
});