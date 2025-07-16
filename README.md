# Contact Converter

Este projeto é um conversor de dados de contatos exportados do [DropDesk](https://www.dropdesk.com.br/) `v2.28.14` para um formato aceito pelo [AtendeChat](https://atendechat.com/) `v6.0.0`.

## :wrench: Dependências
Para executar o programa, você precisa do Python `v3.9.13` (outras versões devem funcionar, dependendo das mudanças).

Além disso, as demais dependências necessárias são listadas no arquivo `requirements.txt`, para conveniência na instalação com o Python.

## :grey_question: Utilização
Para usar, na pasta onde você instalar o repositório, execute o seguinte comando:

``` bash
python ./main.py <input_path> <output_path>
```

Ao executar este comando, o arquivo apontado pelo `<input_path>` será traduzido para um novo arquivo no caminho apontado pelo `<output_path>`.

Se forem necessárias mais informações sobre o programa, você pode passar o parâmetro `-h` ou `--help` para o `main.py`.

## :heart: Créditos
Feito por [Daniel (nadjiel) de Oliveira](https://github.com/nadjiel)
