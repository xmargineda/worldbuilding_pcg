import requests
import time
import multiprocessing
from ontology.onto_manager import * 
from llm_manager import *
from process_manager import *


if __name__ == '__main__':

    main_req_q = multiprocessing.Queue() #This queue sends the requests from the main
    main_res_q = multiprocessing.Queue() #This queue sends the formated results to the main
    llm_req_q = multiprocessing.Queue() #This queue sends the requests to the LLM
    llm_res_q = multiprocessing.Queue() #This queue sends the formated results of the LLM

    pr_pr = multiprocessing.Process(target=process_manager, args=(main_req_q, main_res_q, llm_req_q, llm_res_q))
    pr_llm = multiprocessing.Process(target=llm_manager, args=(llm_req_q, llm_res_q))
    
    try:
        pr_pr.start()
        pr_llm.start()
        loop = True
        while loop:
            print("?- What is your command?\n-raw input\n-exit")
            inp = input()
            if inp == "exit":
                loop = False
            elif inp == "raw input":
                txt = input("Please input here your text:\n")
                main_req_q.put({"func":"raw_input_processing", "txt":txt, 'type':'req'})
                print(onto_res_q.get())
            elif inp == "debug 1":
                main_req_q.put({"func":"debug"})
                
            else:
                print("!- Command not identified\n")
        
        pr_pr.terminate()
        pr_llm.terminate()
        pr_pr.join()
        pr_llm.join()

    except KeyboardInterrupt:
        print("Interrupt caught")
        pr_pr.terminate()
        pr_llm.terminate()
        pr_pr.join()
        pr_llm.join()