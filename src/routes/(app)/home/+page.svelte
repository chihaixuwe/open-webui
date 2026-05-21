<script lang="ts">
	import Chat from '$lib/components/chat/Chat.svelte';
	import { browser } from '$app/environment';
	import { config } from '$lib/stores';

	let immichUrl = '';
	const defaultUrl = browser ? `${location.protocol}//${location.hostname}:3000` : '';

	$: immichUrl = $config?.ui?.immich_url ?? defaultUrl;
</script>

<svelte:head>
	<title>Home</title>
</svelte:head>

<div class="flex flex-col w-full h-full">
	<div class="flex items-center justify-end p-2">
		<a href="/gallery" class="px-3 py-1 rounded bg-blue-600 text-white hover:bg-blue-500">图库</a>
	</div>

	<!-- 上半部分：WebUI 控件（聊天/控制区） -->
	<div class="h-[50vh] overflow-hidden">
		<Chat />
	</div>

	<!-- 下半部分：Immich 图库（iframe 嵌入） -->
	<div class="flex-1 h-[50vh]">
		{#if immichUrl}
			<iframe
				src={immichUrl}
				class="w-full h-full border-0"
				allow="camera; microphone; fullscreen; autoplay; encrypted-media"
				loading="lazy"
			/>
		{:else}
			<div class="p-6 text-center">Gallery URL 未配置。请在后端配置 `config.ui.immich_url` 或访问本地端口 3000。</div>
		{/if}
	</div>
</div>
