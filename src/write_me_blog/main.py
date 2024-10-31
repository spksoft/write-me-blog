#!/usr/bin/env python
import sys
import os
from datetime import datetime

from langtrace_python_sdk import langtrace, with_additional_attributes
from write_me_blog.crew import WriteMeBlogCrew


langtrace.init(api_key = os.getenv('LANGTRACE_API_KEY'))

inputs = {
    "topic": "Understanding Multi-Agent System with CrewAI",
    "blog_intention": "Make audience understand about Multi-Agent System and understand overall concept of CrewAI. such as process, task, agent, environment, memory manager, etc.",
    "language": "Thai",
    "reference": "https://docs.crewai.com/",
    "read_time": 30
}

# user_id is ISODate time
@with_additional_attributes({'user_id': datetime.now().isoformat()}) 
def run():
    """
    Run the crew.
    """
    WriteMeBlogCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    try:
        WriteMeBlogCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        WriteMeBlogCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    try:
        WriteMeBlogCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
