// Gerenciamento de itens do pedido
let itemParaRemover = null;
let contadorItens = 0;

function adicionarItem() {
    if (!window.produtos) {
        console.error('Produtos não carregados');
        return;
    }

    const tbody = document.getElementById('itensBody');
    const row = document.createElement('tr');
    row.id = `item-${contadorItens}`;

    row.innerHTML = `
        <td>
            <select name="itens-${contadorItens}-produto" onchange="atualizarPreco(${contadorItens})" required>
                <option value="">Selecione um produto</option>
                ${Object.entries(window.produtos).map(([id, produto]) =>
                    `<option value="${id}">${produto.titulo}</option>`
                ).join('')}
            </select>
        </td>
        <td>
            <input type="number" name="itens-${contadorItens}-quantidade" min="1" value="1"
                   onchange="calcularSubtotal(${contadorItens})" required style="margin: 0;">
        </td>
        <td>
            <input type="number" name="itens-${contadorItens}-preco" step="0.01" min="0"
                   onchange="calcularSubtotal(${contadorItens})" required style="margin: 0;">
        </td>
        <td>
            <span id="subtotal-${contadorItens}">R$ 0,00</span>
        </td>
        <td>
            <button type="button" onclick="mostrarConfirmacao(${contadorItens})"
                    class="outline" style="margin: 0;">Deletar</button>
        </td>
    `;

    tbody.appendChild(row);
    contadorItens++;
}

function atualizarPreco(itemId) {
    const select = document.querySelector(`select[name="itens-${itemId}-produto"]`);
    const precoInput = document.querySelector(`input[name="itens-${itemId}-preco"]`);

    const produtoId = select.value;
    if (produtoId && window.produtos[produtoId]) {
        precoInput.value = window.produtos[produtoId].preco;
        calcularSubtotal(itemId);
    } else {
        precoInput.value = '';
        document.getElementById(`subtotal-${itemId}`).textContent = 'R$ 0,00';
    }
}

function calcularSubtotal(itemId) {
    const quantidade = parseFloat(document.querySelector(`input[name="itens-${itemId}-quantidade"]`).value) || 0;
    const preco = parseFloat(document.querySelector(`input[name="itens-${itemId}-preco"]`).value) || 0;

    const subtotal = quantidade * preco;
    document.getElementById(`subtotal-${itemId}`).textContent =
        'R$ ' + subtotal.toFixed(2).replace('.', ',');

    calcularTotalGeral();
}

function calcularTotalGeral() {
    const tbody = document.getElementById('itensBody');
    const rows = tbody.querySelectorAll('tr');
    let total = 0;

    rows.forEach(row => {
        const quantidadeInput = row.querySelector('input[name*="-quantidade"]');
        const precoInput = row.querySelector('input[name*="-preco"]');

        if (quantidadeInput && precoInput) {
            const quantidade = parseFloat(quantidadeInput.value) || 0;
            const preco = parseFloat(precoInput.value) || 0;
            total += quantidade * preco;
        }
    });

    const totalElement = document.getElementById('totalGeral');
    if (totalElement) {
        totalElement.textContent = 'R$ ' + total.toFixed(2).replace('.', ',');
    }
}

function mostrarConfirmacao(itemId) {
    itemParaRemover = itemId;
    document.getElementById('confirmDialog').showModal();
}

function confirmarExclusao() {
    if (itemParaRemover !== null) {
        const row = document.getElementById(`item-${itemParaRemover}`);
        if (row) {
            row.remove();
            calcularTotalGeral();
        }
        itemParaRemover = null;
    }
    document.getElementById('confirmDialog').close();
}

function cancelarExclusao() {
    itemParaRemover = null;
    document.getElementById('confirmDialog').close();
}

// Adicionar um item inicial ao carregar a página
document.addEventListener('DOMContentLoaded', function() {
    adicionarItem();
});
