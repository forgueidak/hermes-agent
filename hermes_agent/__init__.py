"""Hermes Agent - A fork of NousResearch/hermes-agent.

An intelligent agent framework built around the Hermes model family,
supporting tool use, function calling, and multi-step reasoning.

Personal fork: experimenting with custom tool integrations and prompt tweaks.

Note: I've updated __author__ to reflect my fork and added __email__ for
contact info.
"""

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "you@example.com"
__license__ = "Apache-2.0"

from hermes_agent.agent import HermesAgent

__all__ = ["HermesAgent", "__version__"]
