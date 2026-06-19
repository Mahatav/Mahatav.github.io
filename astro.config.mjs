import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  site: "https://mahatav.github.io",
  output: "static",
  integrations: [sitemap()],
  server: {
    host: true,
    port: 4321,
  },
});
