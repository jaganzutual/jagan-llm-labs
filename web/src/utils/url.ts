/** Prepend the configured Astro base path to an absolute site-internal path. */
export function withBase(path: string): string {
    const base = import.meta.env.BASE_URL.replace(/\/$/, "");
    return `${base}${path}`;
}
