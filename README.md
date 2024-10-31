# WriteMeBlog Crew (POC)

An AI-powered blog content creation system built with [crewAI](https://crewai.com). This project automates the process of creating high-quality blog content by orchestrating multiple AI agents that work together, each handling different aspects of content creation like research, writing, and editing.

## What It Does

WriteMeBlog Crew helps you create blog content by:
- Researching your chosen topic thoroughly
- Writing engaging and informative blog posts
- Editing and refining the content for clarity and accuracy
- Generating a complete blog post in markdown format

## Installation

Requires Python >=3.10 <=3.13 and [Poetry](https://python-poetry.org/) for dependency management.

1. Install Poetry if you haven't already:
```bash
pip install poetry
```

2. Install project dependencies:
```bash
crewai install
```

## Configuration

1. Create a `.env` file from `.env.example` and add your `OPENAI_API_KEY`
2. Customize your content creation process:
   - `src/write_me_blog/main.py`: Modify input parameters for your blog posts

## Usage

Run the content creation process from the project root:

```bash
crewai run
```

The system will generate a `blog_post.md` file containing your blog post in the `output` directory.

## How It Works

WriteMeBlog Crew uses a team of specialized AI agents that collaborate to create your content:
- `senior_software_engineer`: Researches and writes learning notes about the topic
- `senior_tech_evangelist`: Writes the blog post

Each agent is configured to focus on specific aspects of content creation, ensuring high-quality output.

## License

[MIT License](LICENSE)
