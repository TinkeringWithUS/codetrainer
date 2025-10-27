import { DEV_BACKEND_URL } from "../lib/constants";

export async function backendGetText(url: string) {
    const res = await fetch(url);
    return res.text();
}

export async function backendGetJSON(url?: string) {
    const res = await fetch(url ?? DEV_BACKEND_URL);
    return res.json();
}
