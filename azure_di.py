from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeResult, ContentFormat

endpoint = "<azure endpoint>"
key = "<api key>"


def analyze_layout(file_path: str) -> AnalyzeResult:
    document_intelligence_client = DocumentIntelligenceClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )
    with open(file_path, "rb") as f:
        poller = document_intelligence_client.begin_analyze_document("prebuilt-layout", analyze_request=f, content_type="application/octet-stream", output_content_format=ContentFormat.MARKDOWN,)
        result = poller.result()
    return result


from pathlib import Path
azure_result = analyze_layout(str(Path.home() / "corello.pdf"))
print(azure_result.content)
