# How to convert from ipynb to html
- ipynb 파일을 pdf로 변환하고 싶다.
    - vscode IDE에서 export 명령어는 에러 발생
- 먼저, html로 변환 후, 웹브라우저에서 html을 읽고 인쇄를 pdf 형태로 하는 꼼수 ✨

```bash
$ jupyter nbconvert --to html src/day6-agent-design/d6_pbl_Corrective_RAG.ipynb 
[NbConvertApp] Converting notebook src/day6-agent-design/d6_pbl_Corrective_RAG.ipynb to html
[NbConvertApp] Writing 419921 bytes to src/day6-agent-design/d6_pbl_Corrective_RAG.html
```