<script lang="ts">
import { browser } from '$app/environment';
import { config } from '$lib/stores';

let immichUrl = '';

const defaultUrl = browser ? `${location.protocol}//${location.hostname}:3000` : '';

$: immichUrl = $config?.ui?.immich_url ?? defaultUrl;
</script>

<svelte:head>
  <title>Gallery</title>
</svelte:head>

<div class="w-full h-full">
  {#if immichUrl}
    <iframe
      src={immichUrl}
      class="w-full h-[100dvh] border-0"
      allow="camera; microphone; fullscreen; autoplay; encrypted-media"
      loading="lazy"
    />
  {:else}
    <div class="p-6 text-center">Gallery URL 未配置。请在后端配置 `config.ui.immich_url` 或访问本地端口 3000。</div>
  {/if}
</div>
