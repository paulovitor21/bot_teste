import { createServer } from 'http';
import { readdir } from 'fs/promises'; // Usando fs.promises para ler diretórios de forma assíncrona
import path from 'path';

// Carrega variáveis de ambiente de um arquivo .env
import { config as dotenvConfig } from 'dotenv';

// Função assíncrona para configurar o ambiente e iniciar o servidor
const startServer = async () => {
    // Carrega variáveis de ambiente de um arquivo .env
    await dotenvConfig();

    const server = createServer((req, res) => {
        // Verifica se a rota é '/'
        if (req.url === '/') {
            // Define o diretório a ser listado
            const directoryPath = path.resolve(); // Diretório atual

            // Lê o conteúdo do diretório
            readdir(directoryPath)
                .then(files => {
                    // Formata a lista de arquivos e subdiretórios como HTML
                    const fileList = files.map(file => `<li>${file}</li>`).join('');

                    // Retorna a lista de arquivos e subdiretórios como uma página HTML
                    res.writeHead(200, { 'Content-Type': 'text/html' });
                    res.end(`
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <title>Lista de Arquivos e Subdiretórios</title>
                        </head>
                        <body>
                            <h1>Arquivos e Subdiretórios em ${directoryPath}</h1>
                            <ul>${fileList}</ul>
                        </body>
                        </html>
                    `);
                })
                .catch(err => {
                    // Em caso de erro, retorna uma resposta de erro
                    res.writeHead(500, { 'Content-Type': 'text/plain' });
                    res.end('Erro ao ler o diretório.');
                });
        } else {
            // Se a rota não for '/', retorna uma resposta de "Página não encontrada"
            res.writeHead(404, { 'Content-Type': 'text/plain' });
            res.end('Página não encontrada.');
        }
    });

    const PORT = process.env.PORT || 3000;
    server.listen(PORT, () => {
        console.log(`Servidor rodando em http://localhost:${PORT}`);
    });
};

// Chama a função startServer para iniciar o servidor
startServer();
