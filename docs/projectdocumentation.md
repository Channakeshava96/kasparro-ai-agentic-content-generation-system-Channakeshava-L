# Multi-Agent Content Generation System


## Problem Statement

The objective of this assignment is to design and implement a modular, agentic automation system that takes a structured product dataset as input and automatically generates machine-readable content pages.

The focus of this challenge is not on content creativity or domain expertise, but on system design, agent orchestration, reusable logic, and structured output generation. The system must operate deterministically, without relying on external data sources or monolithic prompt-based solutions.


## Solution Overview

The solution is implemented as a multi-agent content generation pipeline. Each agent in the system has a single, well-defined responsibility and operates on structured inputs and outputs.

The system follows a clear orchestration flow where raw product data is parsed into an internal model, processed by specialized agents, transformed using reusable logic blocks, and assembled into structured JSON content pages using custom templates.

The final output consists of three machine-readable JSON pages:
- FAQ Page
- Product Description Page
- Comparison Page (against a fictional product)

## Scope & Assumptions

- The system operates strictly on the provided product dataset.
- No external facts, APIs, or research are used.
- Product data follows a consistent, known schema.
- Product comparison uses a fictional, internally defined competitor product.
- The system prioritizes structural correctness and reusability over content quality.
- All outputs are generated in JSON format for downstream consumption.


## System Design

The architecture follows an orchestrator-driven, multi-agent design pattern.

### Core Design Principles
- Single responsibility per agent
- Explicit input/output contracts
- No shared global state
- Deterministic execution flow
- Reusable and composable logic blocks

### Agent Roles

- **ProductParserAgent**  
  Converts raw product input into a clean internal Product model.

- **QuestionGenerationAgent**  
  Generates categorized user questions based on product attributes.

- **FAQPageAgent**  
  Assembles the FAQ page using generated questions and logic blocks.

- **ProductPageAgent**  
  Constructs the product description page using reusable content logic blocks.

- **ComparisonPageAgent**  
  Generates a structured comparison page between the main product and a fictional competitor.

### Reusable Logic Blocks

Logic blocks are implemented as pure functions responsible for transforming product data into structured content units. These blocks are reused across multiple page types to ensure composability and consistency.

Examples include:
- benefit generation
- usage extraction
- safety information handling
- product comparison

### Template System

The system includes a custom template layer where each page type defines:
- required content blocks
- structural rules
- output schema expectations

Templates are declarative and do not generate content directly. They act as contracts that page assembly agents must satisfy.

### Orchestration Flow

The full pipeline is coordinated by a single orchestrator that executes agents in a deterministic order:


Raw Product Data
↓
ProductParserAgent
↓
QuestionGenerationAgent
↓
Page Assembly Agents
↓
JSON Output Pages



All page generation is performed via agents, ensuring the system is modular, extensible, and production-aligned.

## High-Level Flow Diagram

![Multi-Agent Content Generation System Workflow](images/system_workflow.png)

*Figure: Orchestrator-driven workflow of the multi-agent content generation system.*