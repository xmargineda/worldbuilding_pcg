from owlready2 import *
import time



def ontology_manager(llm_res_q, onto_req_q, onto_res_q):
    onto = get_ontology("file://ontology/ontoTFG.owl").load()

    while True:
        while llm_res_q.empty() and onto_req_q.empty():
            time.sleep(0.1)
        if not onto_req_q.empty():
            ## Here request from onto_req_q are treated, normally queries about the ontology
            onto_req_q.get()
            onto_res_q.put("ONTO: IM SAYING HELLO")

        if not llm_res_q.empty():
            ## Here results from llm_res_q are treated, normally individuals to add to the ontology
            print(b)


        

            

        



