import {Viewer} from "./Viewer";

interface QWebChannelTransport {
    // Transport interface from Qt WebChannel
}

interface QtWebChannel {
    webChannelTransport: QWebChannelTransport;
}

declare const QWebChannel: any;

interface BridgeSignal {
    connect(callback: (...args: any[]) => void): void;

    disconnect(callback: (...args: any[]) => void): void;
}

export interface Bridge {
    addXyzModel: BridgeSignal;
    addCifModel: BridgeSignal;
    resetView: BridgeSignal;
    setView: BridgeSignal;

    viewChanged(viewState: any): void;

    logFromJs(message: string): void;

    receive(obj: any): void;
}

interface QWebChannelObjects {
    bridge: Bridge;
}

interface QWebChannelInstance {
    objects: QWebChannelObjects;
}

type QWebChannelConstructor = new (
    transport: QWebChannelTransport,
    callback: (channel: QWebChannelInstance) => void
) => void;

// Extend Window interface
declare global {
    interface Window {
        QWebChannel?: QWebChannelConstructor;
        qt?: QtWebChannel;
    }
}

export function setupWebChannel(container: HTMLElement, onSetupWebChanel: (viewer: Viewer) => void): void {
    if (
        typeof window.QWebChannel !== "undefined" &&
        typeof window.qt !== "undefined" &&
        window.qt.webChannelTransport
    ) {
        new window.QWebChannel(window.qt.webChannelTransport, (channel: QWebChannelInstance) => {
            console.log("Channel connected:", Object.keys(channel));
            console.log("Available objects:", Object.keys(channel.objects));

            const bridge: Bridge = channel.objects.bridge;

            const viewer = new Viewer(container, bridge);

            onSetupWebChanel(viewer);
        });
    } else {
        setTimeout(setupWebChannel, 200);
    }
}

export interface Vec3 {
    x: number;
    y: number;
    z: number;
}

export interface Quat {
    w: number;
    x: number;
    y: number;
    z: number;
}

export interface ViewerState {
    posZ: number;
    q: Quat;
    t: Vec3;
}
