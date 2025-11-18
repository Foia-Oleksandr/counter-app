import {type AtomStyleSpec, type BoxSpec, GLViewer} from "3dmol";
import type { ViewerSpec} from "3dmol";
type ViewState = [
    posX: number,
    posY: number,
    posZ: number,
    rotationZ: number,
    qx: number,
    qy: number,
    qz: number,
    qw: number
];

export class Viewer {
    private glViewer: GLViewer;
    private currentViewVector: ViewState | undefined;

    constructor(container: HTMLElement) {
        const viewerConfig: ViewerSpec = {
            backgroundColor: "white"
        }
        this.glViewer = new GLViewer(container, viewerConfig);
        this.glViewer.setViewChangeCallback(() => this.updateViewInfo)
    }

    updateViewInfo(viewState: ViewState) {
        const [
            tx, ty, tz,
            posZ,
            qx, qy, qz, qw
        ] = viewState;

        this.currentViewVector = [tx, ty, tz, posZ, qx, qy, qz, qw];
        console.log(this.currentViewVector);
    // if (window._bridge) {
    //     window._bridge.viewUpdated({tx: tx, ty: ty, tz: tz, posZ: posZ, qx: qx, qy: qy, qz: qz, qw: qw}, updateCount)
    // }
    }

    addBox(box: BoxSpec) {
        this.glViewer.addBox(box);
    }

    render() {
        this.glViewer.zoomTo();
        this.glViewer.render();
    }

    setStyle(atomStyle: AtomStyleSpec) {
        this.glViewer.setStyle(atomStyle);
    }
}