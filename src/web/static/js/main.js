async function processText() {
    const text = document.getElementById('input-text').value;
    const operation = document.getElementById('operation').value;
    
    let data = { text, operation };
    if (operation === 'find_all_occurrences') {
        const substring = prompt('Enter the substring to search for:');
        if (substring === null) return; // User cancelled
        data.substring = substring;
    }
    
    try {
        const response = await fetch('/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });
        
        const responseData = await response.json();
        document.getElementById('result').textContent = responseData.result;
        saveToHistory(text, operation, responseData.result);
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').textContent = 'An error occurred';
    }
}

function copyToClipboard() {
    const result = document.getElementById('result').textContent;
    navigator.clipboard.writeText(result)
        .then(() => {
            showToast('Copied to clipboard!');
        })
        .catch(err => {
            console.error('Failed to copy:', err);
        });
}

function showToast(message) {
    const toast = document.createElement('div');
    toast.className = 'toast show position-fixed bottom-0 end-0 m-3';
    toast.innerHTML = `
        <div class="toast-body">
            ${message}
        </div>
    `;
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 3000);
}

const MAX_HISTORY = 5;

function saveToHistory(text, operation, result) {
    let history = JSON.parse(localStorage.getItem('processingHistory') || '[]');
    history.unshift({ text, operation, result, timestamp: new Date() });
    history = history.slice(0, MAX_HISTORY);
    localStorage.setItem('processingHistory', JSON.stringify(history));
    updateHistoryUI();
}

function updateHistoryUI() {
    const historyList = document.getElementById('history-list');
    const history = JSON.parse(localStorage.getItem('processingHistory') || '[]');
    
    historyList.innerHTML = history.map(item => `
        <div class="list-group-item">
            <div class="d-flex w-100 justify-content-between">
                <h6 class="mb-1">${item.operation.replace(/_/g, ' ').toUpperCase()}</h6>
                <small>${new Date(item.timestamp).toLocaleString()}</small>
            </div>
            <p class="mb-1"><small>Input: ${item.text.substring(0, 50)}${item.text.length > 50 ? '...' : ''}</small></p>
            <small>Result: ${item.result}</small>
        </div>
    `).join('');
}

// Add this line to load history when page loads
document.addEventListener('DOMContentLoaded', updateHistoryUI);