# Gerador de Senhas 🔒

Um programa em Python simples, para gerar senhas aleatórias.

## 📋 Descrição

Este script oferece:
- Geração de senhas aleatórias contendo letras (maiúsculas e minúsculas), números e símbolos
- Histórico das senhas geradas 
- Interface simples em linha de comando

## ⚙️ Funcionalidades

✔️ Gera senhas seguras usando o módulo `secrets` (criptograficamente seguro)  
✔️ Permite visualizar o histórico de senhas geradas
✔️ Interface intuitiva com menu interativo  
✔️ Validação de entrada do usuário  

## 🚀 Como Usar

1. Certifique-se de ter Python 3 instalado
2. Execute o script:
   ```bash
   python gerador_de_senhas.py
   ```
3. No menu:
   - Digite `1` para gerar nova senha
   - Digite `2` para ver o histórico
   - Digite `3` para sair

## 📝 Exemplo de Uso

```
----------------------- MENU PRINCIPAL -----------------------
------------------------------------------------------------
               [1] Gerar nova senha                          
               [2] Ver histórico de senhas                  
               [3] Sair                                     
------------------------------------------------------------
            Escolha uma opção: 1                            
               Nova senha: aB4#k9!L                         
------------------------------------------------------------
```

## 📦 Dependências

- Python 3.x
- Módulos padrão:
  - `secrets`
  - `string`
  - `time`

## ⚠️ Importante

- As senhas são exibidas apenas no terminal e não são armazenadas permanentemente
- Para maior segurança, feche o terminal após usar para limpar o histórico

## 📜 Licença

Este projeto está licenciado sob a licença MIT.
