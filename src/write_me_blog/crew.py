from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool, SerperDevTool

scrape_website_tool = ScrapeWebsiteTool()
serper_tool = SerperDevTool()
@CrewBase
class WriteMeBlogCrew():
	"""WriteMeBlog crew"""

	@agent
	def senior_software_engineer(self) -> Agent:
		return Agent(
			llm="claude-3-5-sonnet-20241022",
			tools=[scrape_website_tool, serper_tool],
			verbose=True,
			config=self.agents_config["senior_software_engineer"]
		)
  
	@agent
	def senior_tech_evangelist(self) -> Agent:
		return Agent(
			llm="claude-3-5-sonnet-20241022",
			tools=[scrape_website_tool, serper_tool],
			verbose=True,
			config=self.agents_config["senior_tech_evangelist"]
		)
  
	@task
	def learn_about_topic_task(self) -> Task:
		return Task(
			config=self.tasks_config["learn_about_topic_task"]
		)
  
	@task
	def write_blog_post_task(self) -> Task:
		return Task(
			config=self.tasks_config["write_blog_post_task"]
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the WriteMeBlog crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.hierarchical,
			manager_llm="claude-3-5-sonnet-20241022",
			verbose=True,
			memory=False,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)