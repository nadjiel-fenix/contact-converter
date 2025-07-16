import openpyxl
import re


def extract_phone(text: str) -> str:
    """
    Valida se uma string representa um número de telefone, e retorna
    sua versão padronizada no formato E.164 (sem o +).
    Se a string não é um número de telefone, entretanto, esta
    função retorna uma string vazia.
    """

    # Remove caracteres não numéricos.
    result = re.sub(r"\D", "", text)

    # Remove 0 inicial, se presente.
    if result.startswith("0"):
        result = result[1:]

    # Remove código do Brasil, se houver.
    if result.startswith("55") and len(result) > 11:
        result = result[2:]

    # Valida tamanho do número: 10 (fixo) or 11 (celular).
    if len(result) in [10, 11]:
        return "55" + result

    return result if len(result) in [10, 11] else ""


def convert(input_path: str, output_path: str):
    # Carregar workbook do DropDesk.
    in_wb = openpyxl.load_workbook(input_path)
    # Carrega o worksheet padrão, que se
    # espera que contenha os dados exportados.
    in_ws = in_wb.active

    # Extrai os headers
    headers = [
        cell.value.strip() if cell.value else ""
        for cell in next(in_ws.iter_rows(min_row=1, max_row=1))
    ]
    header_map = {h: i for i, h in enumerate(headers)}

    # Prepara novo workbook para output.
    out_wb = openpyxl.Workbook()
    out_ws = out_wb.active
    # Adiciona headers esperados pelo AtendeChat
    out_ws.append(["Nome", "Telefone"])

    for row in in_ws.iter_rows(min_row=2):
        nome = row[header_map["Nome"]].value or ""
        empresa = row[header_map["Empresa"]].value or ""
        telefone = row[header_map["Telefone"]].value or ""

        nome_final = nome.strip() if nome.strip() else empresa.strip()
        telefone_final = extract_phone(telefone) or extract_phone(empresa)

        out_ws.append([nome_final, telefone_final])

    out_wb.save(output_path)


# Conversão de arquivos padrões.
convert(input_path="dropdesk_contacts.xlsx", output_path="atendechat_contacts.xlsx")
