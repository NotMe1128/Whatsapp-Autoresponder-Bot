import re
from googlesearch import search
from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor

def process_input(input_str):

    try:
        query = input_str[len("!google"):].strip()
        print(query)
        search_results = list(search(query, num_results=3))
        summarizer = AutoAbstractor()
        summarizer.tokenizable_doc = SimpleTokenizer()
        summarizer.delimiter_list = [".", "\n"]
        abstractor = TopNRankAbstractor()
        result_dict = summarizer.summarize(" ".join(search_results), abstractor)
        return "\n".join(result_dict["summarize_result"])
    except Exception as e:
        return f"{e}"
