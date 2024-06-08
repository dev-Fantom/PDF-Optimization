# Script for PDF Optimization / PDFを軽量化するスクリプト

This script optimizes PDF files and outputs them in a reduced size.



PDFを軽量化して出力します。

## Environment / 環境

* Python 3.11.6
* Ghostscript 10.03.1

## Usage / 使い方

Install Ghostscript using Homebrew. (Skip this step if Ghostscript is already installed)

HomebrewでGhostscriptをインストールします。（既にインストールされていれば飛ばします）

```shell
  brew install ghostscript
```

## Sample usage / 実行方法

When running the python command, specify the path of the PDF to be optimized and the quality of the output resolution.

pythonコマンドを実行する際に軽量化するPDFのパスと出力する解像度のクオリティを指定します。

### Quality (Resolution) / クオリティ（解像度）

* screen: 72
* ebook: 150
* printer: 300
* prepress: 300
* default: 300

```shell
  python comp.py /path/to/your/input.pdf ebook
```

## Results / 出力結果

The optimized file will be output to the outputs directory.

軽量化したファイルがoutputsに出力されます。

## Author / 作成者

- [Fantom, Inc. (JP)](https://twitter.com/Fantomcojp)
