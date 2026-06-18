import { defineConfig } from "astro/config";

export default defineConfig({
  site: "https://mahatav.dev",
  output: "static",
  server: {
    host: true,
    port: 4321,
  },
});
