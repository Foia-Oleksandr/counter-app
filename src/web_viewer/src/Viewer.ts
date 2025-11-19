import {type AtomStyleSpec, type BoxSpec, GLViewer, type SphereSpec} from "3dmol";
import type {ViewerSpec} from "3dmol";
import type {Bridge, ViewerState} from "./web-chanel-interface";


type GLViewState = [
    posX: number,
    posY: number,
    posZ: number,
    zoom: number,
    qx: number,
    qy: number,
    qz: number,
    qw: number
];

function toGLViewState(v: ViewerState): GLViewState {
    return [
        v.t.x,
        v.t.y,
        v.t.z,
        v.posZ,
        v.q.x,
        v.q.y,
        v.q.z,
        v.q.w
    ];
}

export class Viewer {
    private readonly glViewer: GLViewer;
    private initialViewVector: GLViewState | undefined;
    private readonly bridge: Bridge;

    constructor(container: HTMLElement, bridge: Bridge) {
        this.bridge = bridge;
        const viewerConfig: ViewerSpec = {
            backgroundColor: "white"
        }
        this.glViewer = new GLViewer(container, viewerConfig);

        this.glViewer.setViewChangeCallback(this.updateViewInfo)

        this.configureBridge();
        console.log("Bridge configured");
    }

    configureBridge = () => {
        console.log("Bridge signals: ", Object.keys(this.bridge));

        this.bridge.addXyzModel.connect(this.addXyzModel);
        this.bridge.addCifModel.connect(this.addCifModel);
        this.bridge.resetView.connect(this.resetView);
        this.bridge.setView.connect(this.setView);

        this.bridge.logFromJs("Web channel setup complete")
    }

    addXyzModel = (xyzData: string) => {
        this.glViewer.addModel(xyzData, "xyz");
    }

    addCifModel = (cifData: string) => {
        this.glViewer.addModel(cifData, "cif");
    }

    resetView = () => {
        this.glViewer.setView(this.initialViewVector)
    }

    setView = (viewerState: ViewerState) => {
        const glViewState = toGLViewState(viewerState);
        this.glViewer.setView(glViewState);
    }

    updateViewInfo = (glViewState: GLViewState) => {
        const [
            tx, ty, tz,
            posZ,
            qx, qy, qz, qw
        ] = glViewState;

        const viewerState: ViewerState = {
            t: {x: tx, y: ty, z: tz},
            posZ: posZ,
            q: {x: qx, y: qy, z: qz, w: qw}
        };
        this.bridge.viewChanged(viewerState);
    }

    addBox = (box: BoxSpec) => {
        this.glViewer.addBox(box);
    }

    render() {
        this.glViewer.zoomTo();
        this.glViewer.render(this.storeView);
    }

    storeView = () => {
        const [
            tx, ty, tz,
            posZ,
            qx, qy, qz, qw
        ] = this.glViewer.getView();
        this.initialViewVector = [tx, ty, tz, posZ, qx, qy, qz, qw];
    }

    setStyle = (atomStyle: AtomStyleSpec) => {
        this.glViewer.setStyle(atomStyle);
    }

    addSphere = (sphere: SphereSpec) => {
        this.glViewer.addSphere(sphere);
    }
}