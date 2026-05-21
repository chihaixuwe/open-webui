<script lang="ts">
  let messages = $state<Array<{ id: number; role: 'user' | 'assistant'; text: string }>>([
    { id: 1, role: 'assistant', text: '你好！我可以帮你分析图像、生成描述，或者回答任何问题。有什么可以帮你的吗？' }
  ]);
  let inputText = $state('');
  let isLoading = $state(false);
  let isOpen = $state(true);

  async function sendMessage() {

    const userMessage = {
      id: Date.now(),
      role: 'user' as const,
      text: inputText
    };

    messages = [...messages, userMessage];
    const currentInput = inputText;
    inputText = '';
    isLoading = true;

    setTimeout(() => {
      const assistantMessage = {
        id: Date.now() + 1,
        role: 'assistant' as const,
        text: '这是一个示例回复。在实际使用中，这里会连接到您的 AI 后端来获取真实响应。'
      };
      messages = [...messages, assistantMessage];
      isLoading = false;
    }, 1000);
  }

  function handleKeyDown(e: KeyboardEvent) {
      e.preventDefault();
      sendMessage();
    }
  }

  function togglePanel() {
  }
</script>

<div class="ai-panel">
  <div class="panel-toggle" on:click={togglePanel}>
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <circle cx="12" cy="12" r="10" />
      <path d="M8 12h8M12 8v8" />
    </svg>
    <span>AI 助手</span>
  </div>

  {#if isOpen}
    <div class="panel-content">
      <div class="panel-header">
        <span class="panel-title">AI 对话</span>
        <button class="close-btn" on:click={togglePanel}>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="18" y1="6" x2="6" y2="18" />
            <line x1="6" y1="6" x2="18" y2="18" />
          </svg>
        </button>
      </div>

      <div class="messages-container">
        {#if messages.length === 1}
          <div class="welcome-section">
            <div class="welcome-icon">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <circle cx="12" cy="12" r="10" />
                <path d="M8 12h8M12 8v8" />
              </svg>
            </div>
            <h3>你好！</h3>
            <p>选择一张图片或输入问题开始对话</p>
            <div class="quick-actions">
              <button class="quick-btn">分析图片</button>
              <button class="quick-btn">生成描述</button>
              <button class="quick-btn">识别内容</button>
            </div>
          </div>
        {:else}
          <div class="messages">
            {#each messages as message (message.id)}
              <div class="message {message.role}">
                {#if message.role === 'assistant'}
                  <div class="avatar">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <circle cx="12" cy="12" r="10" />
                      <path d="M8 12h8M12 8v8" />
                    </svg>
                  </div>
                {/if}
                <div class="message-content">
                  {message.text}
                </div>
                {#if message.role === 'user'}
                  <div class="avatar user">
                    <span>U</span>
                  </div>
                {/if}
              </div>
            {/each}

            {#if isLoading}
              <div class="message assistant">
                <div class="avatar">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10" />
                    <path d="M8 12h8M12 8v8" />
                  </svg>
                </div>
                <div class="message-content typing">
                  <span></span>
                  <span></span>
                  <span></span>
                </div>
              </div>
            {/if}
          </div>
        {/if}
      </div>

      <div class="input-area">
        <div class="input-wrapper">
          <button class="attach-btn">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M21.44 11.05l-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48" />
            </svg>
          </button>
          <textarea
            bind:value={inputText}
            placeholder="输入你的问题..."
            on:keydown={handleKeyDown}
            disabled={isLoading}
            rows="1"
          />
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
              <circle cx="12" cy="12" r="10" fill="black" />
              <path d="M8 12h8M12 8v8" stroke="white" />
            </svg>
          </button>
        </div>
      </div>
    </div>
  {/if}
</div>

<style>
  .ai-panel {
    position: fixed;
    right: 0;
    top: 0;
    height: 100vh;
    z-index: 1000;
    display: flex;
    flex-direction: row;
  }

  .panel-toggle {
    position: absolute;
    right: 100%;
    top: 50%;
    transform: translateY(-50%);
    background: #1f2937;
    color: white;
    border: none;
    border-radius: 8px 0 0 8px;
    padding: 16px 12px;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
    font-size: 0.8rem;
    box-shadow: -2px 0 8px rgba(0,0,0,0.1);
    transition: background 0.2s;
  }

  .panel-toggle:hover {
    background: #374151;
  }

  .panel-content {
    width: 420px;
    height: 100%;
    background: #f9fafb;
    border-left: 1px solid #e5e7eb;
    display: flex;
    flex-direction: column;
    box-shadow: -4px 0 20px rgba(0,0,0,0.08);
  }

  .panel-header {
    padding: 16px 20px;
    background: white;
    border-bottom: 1px solid #e5e7eb;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .panel-title {
    font-size: 1rem;
    font-weight: 600;
    color: #111827;
  }

  .close-btn {
    width: 32px;
    height: 32px;
    border: none;
    background: transparent;
    border-radius: 6px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #6b7280;
    transition: background 0.2s;
  }

  .close-btn:hover {
    background: #f3f4f6;
  }

  .messages-container {
    flex: 1;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
  }

  .welcome-section {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 40px 24px;
    text-align: center;
  }

  .welcome-icon {
    width: 64px;
    height: 64px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    margin-bottom: 20px;
  }

  .welcome-section h3 {
    margin: 0 0 8px;
    font-size: 1.3rem;
    color: #111827;
  }

  .welcome-section p {
    margin: 0 0 24px;
    color: #6b7280;
    font-size: 0.95rem;
  }

  .quick-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    justify-content: center;
  }

  .quick-btn {
    padding: 10px 16px;
    background: white;
    border: 1px solid #d1d5db;
    border-radius: 20px;
    font-size: 0.85rem;
    color: #374151;
    cursor: pointer;
    transition: all 0.2s;
  }

  .quick-btn:hover {
    background: #f3f4f6;
    border-color: #9ca3af;
  }

  .messages {
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .message {
    display: flex;
    gap: 12px;
    align-items: flex-start;
  }

  .message.user {
    flex-direction: row-reverse;
  }

  .avatar {
    width: 32px;
    height: 32px;
    background: #e5e7eb;
    border-radius: 6px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    color: #374151;
  }

  .avatar.user {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: 50%;
    font-weight: 600;
    font-size: 0.9rem;
  }

  .message-content {
    flex: 1;
    padding: 12px 16px;
    background: white;
    border-radius: 12px;
    line-height: 1.6;
    color: #111827;
    font-size: 0.95rem;
    border: 1px solid #e5e7eb;
  }

  .message.user .message-content {
    background: #1f2937;
    color: white;
    border-color: #1f2937;
  }

  .message-content.typing {
    display: flex;
    gap: 4px;
    padding: 16px;
  }

  .message-content.typing span {
    width: 6px;
    height: 6px;
    background: #6b7280;
    border-radius: 50%;
    animation: typing 1.4s infinite;
  }

  .message-content.typing span:nth-child(2) {
    animation-delay: 0.2s;
  }

  .message-content.typing span:nth-child(3) {
    animation-delay: 0.4s;
  }

  @keyframes typing {
    0%, 60%, 100% {
      transform: translateY(0);
      opacity: 0.4;
    }
    30% {
      transform: translateY(-6px);
      opacity: 1;
    }
  }

  .input-area {
    padding: 16px;
    background: white;
    border-top: 1px solid #e5e7eb;
  }

  .input-wrapper {
    display: flex;
    align-items: flex-end;
    gap: 8px;
    background: #f3f4f6;
    border: 1px solid #e5e7eb;
    border-radius: 24px;
    padding: 8px 12px;
  }

  .attach-btn {
    width: 36px;
    height: 36px;
    border: none;
    background: transparent;
    border-radius: 50%;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #6b7280;
    transition: background 0.2s;
    flex-shrink: 0;
  }

  .attach-btn:hover {
    background: #e5e7eb;
  }

  .input-wrapper textarea {
    flex: 1;
    padding: 8px 12px;
    background: transparent;
    border: none;
    color: #111827;
    font-size: 0.95rem;
    resize: none;
    min-height: 24px;
    max-height: 120px;
    line-height: 1.5;
  }

  .input-wrapper textarea:focus {
    outline: none;
  }

  .input-wrapper textarea::placeholder {
    color: #9ca3af;
  }

  .send-btn {
    width: 36px;
    height: 36px;
    background: #1f2937;
    border: none;
    border-radius: 50%;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: opacity 0.2s;
    flex-shrink: 0;
  }

  .send-btn:hover:not(:disabled) {
    opacity: 0.9;
  }

  .send-btn:disabled {
    opacity: 0.4;
    cursor: not-allowed;
  }
</style>
