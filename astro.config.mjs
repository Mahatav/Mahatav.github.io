import { defineConfig } from "astro/config";

export default defineConfig({
  site: "https://mahatav.github.io",
  output: "static",
  server: {
    host: true,
    port: 4321,
  },
});
