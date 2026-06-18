import { defineConfig } from "astro/config";
import process from "node:process";

const isGithubPagesBuild = process.env.GITHUB_ACTIONS === "true";
const repoName = process.env.GITHUB_REPOSITORY?.split("/")[1] ?? "";
const base = process.env.DEPLOY_BASE ?? (isGithubPagesBuild && repoName ? `/${repoName}` : "/");

export default defineConfig({
  site: "https://mahatav.dev",
  base,
  output: "static",
  server: {
    host: true,
    port: 4321,
  },
});
