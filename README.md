# TIFF to PDF Converter

## English

This project is a TIFF to PDF converter that allows bulk conversion of all TIFF files in a specific directory. The script can generate multiple PDFs, one for each TIFF file, or combine all files into a single PDF, with each image on a separate page.

### Features

- **Bulk Conversion**: Converts all TIFF files in an input directory.
- **PDF Generation Modes**:
  - **Multiple PDFs**: Generates a separate PDF for each TIFF file.
  - **Single PDF**: Combines all TIFF files into a single PDF, with each image on a different page.
- **Customizable Settings**: Allows you to adjust the resolution (DPI), width, and height of the pages in the generated PDF.

## Português

Este projeto é um conversor de arquivos TIFF para PDF, permitindo a conversão em massa de todos os arquivos TIFF em um diretório específico. O script pode gerar múltiplos PDFs, um para cada arquivo TIFF, ou combinar todos os arquivos em um único PDF, com cada imagem em uma página separada.

### Funcionalidades

- **Conversão em Massa**: Converte todos os arquivos TIFF em um diretório de entrada.
- **Modos de Geração de PDF**:
  - **Múltiplos PDFs**: Gera um PDF separado para cada arquivo TIFF.
  - **PDF Único**: Combina todos os arquivos TIFF em um único PDF, com cada imagem em uma página diferente.
- **Configurações Personalizáveis**: Permite ajustar a resolução (DPI), largura e altura das páginas no PDF gerado.

## Prerequisites / Pré-requisitos

Before running the project, you need to have Python installed on your machine. You will also need to install the following dependencies:

Antes de executar o projeto, você precisa ter o Python instalado em sua máquina. Você também precisará instalar as seguintes dependências:

- `PyMuPDF`
- `Pillow`

## Installation of Dependencies / Instalação das Dependências

To install the necessary dependencies, you can use `pip`. Run the following command in the terminal:

Para instalar as dependências necessárias, você pode usar o `pip`. Execute o seguinte comando no terminal:

```bash
pip install PyMuPDF Pillow
```

## How to Use / Como Usar

You can run the script directly in the terminal. Here are the available commands:

Você pode executar o script diretamente no terminal. Aqui estão os comandos disponíveis:

```bash
python tiff_to_pdf.py -i <input_directory> -o <output_directory> -p <pdf_mode> -d <dpi> -w <width> -H <height>
```

### Parameters / Parâmetros

- `-i`, `--input`: Input directory containing TIFF files. (Default: current directory)
- `-o`, `--output`: Output directory for generated PDFs. (Default: `output` in the current directory)
- `-p`, `--pdf`: PDF generation mode: `multiple` for separate PDFs, `unique` for a single PDF. (Default: `multiple`)
- `-d`, `--dpi`: Resolution (DPI) for images in the PDF. (Default: 300)
- `-w`, `--width`: Page width in pixels. (Optional)
- `-H`, `--height`: Page height in pixels. (Optional)

- `-i`, `--input`: Diretório de entrada contendo arquivos TIFF. (Padrão: diretório atual)
- `-o`, `--output`: Diretório de saída para os PDFs gerados. (Padrão: `output` no diretório atual)
- `-p`, `--pdf`: Modo de geração de PDF: `multiple` para PDFs separados, `unique` para um único PDF. (Padrão: `multiple`)
- `-d`, `--dpi`: Resolução (DPI) para as imagens no PDF. (Padrão: 300)
- `-w`, `--width`: Largura da página em pixels. (Opcional)
- `-H`, `--height`: Altura da página em pixels. (Opcional)

### Example Usage / Exemplo de Uso

To convert all TIFF files in a specific directory to separate PDFs, you can use the following command:

Para converter todos os arquivos TIFF em um diretório específico para PDFs separados, você pode usar o seguinte comando:

```bash
python tiff_to_pdf.py -i /path/to/tiff/directory -o /path/to/output/directory -p multiple
```

To generate a single PDF from all TIFF files:

Para gerar um único PDF a partir de todos os arquivos TIFF:

```bash
python tiff_to_pdf.py -i /path/to/tiff/directory -o /path/to/output/directory -p unique
```
