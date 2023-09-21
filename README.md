<!DOCTYPE html>
<html>

<body>
  <h1>Projeto de Precificação com PySimpleGUI e Google Sheets API</h1>
  <p>Este é um projeto Python que utiliza a biblioteca PySimpleGUI para criar uma interface gráfica simples e interativa para calcular o preço de venda de produtos com base no preço de fornecedor, imposto de importação sobre o produto e markup. Além disso, ele se integra ao Google Sheets para armazenar os dados dos produtos.</p>

  <h2>Pré-requisitos</h2>
  <p>Antes de usar este projeto, você precisa ter os seguintes pré-requisitos instalados:</p>
  <ul>
    <li>Python</li>
    <li>As bibliotecas PySimpleGUI, gspread e oauth2client instaladas. Você pode instalá-las com o seguinte comando:</li>
  </ul>

  <pre><code>pip install PySimpleGUI gspread oauth2client</code></pre>

  <p>Uma conta no Google Drive e acesso ao Google Sheets API.</p>
  <p>Um arquivo de credenciais JSON do Google Sheets API (gerado na <a href="https://console.cloud.google.com/" target="_blank">Google Cloud Console</a>).</p>

  <h2>Configuração</h2>
  <p>Siga estas etapas para configurar o projeto:</p>
  <ol>
    <li>Clone ou faça o download deste repositório para o seu computador.</li>
    <li>Coloque o arquivo de credenciais JSON (gerado na etapa anterior) na mesma pasta do projeto com o nome <code>credentials.json</code>.</li>
  </ol>

  <h2>Uso</h2>
  <ol>
    <li>Execute o arquivo <code>precificador.py</code> para iniciar o aplicativo de precificação.</li>
    <li>Preencha as informações solicitadas na interface:</li>
    <ul>
      <li>Produto: Nome do produto.</li>
      <li>Preço Fornecedor: Preço de compra do produto no fornecedor.</li>
      <li>Markup: O markup desejado.</li>
    </ul>
    <li>Clique no botão "Precificar" para calcular o preço de venda e armazenar os dados no Google Sheets.</li>
    <li>Você pode clicar no botão "Limpar" para limpar os campos de entrada.</li>
    <li>Quando terminar, clique no botão "Sair" para fechar o aplicativo.</li>
  </ol>

  <h2>Galeria</h2>
  <h3 ><strong>Precificador</strong></h3>
  <img src="/img/Programa.png" width="400">
  <h3><strong>Planilha</strong> </h3>
  <img src="/img/planilha.png" width="400">
  <h3><strong>Cálculo</strong> </h3>
  <img src=".//img/cadastro.png" width="440">
 


  <h2>Contribuições</h2>
  <p>Contribuições são bem-vindas! Se você deseja melhorar este projeto, sinta-se à vontade para abrir uma issue ou criar um pull request.</p>
</body>

</html>
