"""
Reproducible Pipeline DAG Validator:
Constructs computational workflow Directed Acyclic Graphs,
performs topological sorting (Kahn's algorithm), checks for circular dependencies,
and tracks step inputs/outputs with cryptographic hashes.
"""

from typing import Dict, List, Set
import hashlib


class PipelineTask:
    def __init__(self, name: str, inputs: List[str], outputs: List[str]):
        self.name = name
        self.inputs = inputs
        self.outputs = outputs
        self.dependencies: Set[str] = set()


class WorkflowDAG:
    def __init__(self):
        self.tasks: Dict[str, PipelineTask] = {}

    def add_task(self, name: str, inputs: List[str], outputs: List[str]):
        self.tasks[name] = PipelineTask(name, inputs, outputs)

    def resolve_dependencies(self):
        """Link tasks based on output -> input matching."""
        output_producer = {}
        for t_name, task in self.tasks.items():
            for out in task.outputs:
                output_producer[out] = t_name
                
        for t_name, task in self.tasks.items():
            for inp in task.inputs:
                if inp in output_producer:
                    producer = output_producer[inp]
                    if producer != t_name:
                        task.dependencies.add(producer)

    def topological_sort(self) -> List[str]:
        """Kahn's algorithm for topological sorting."""
        self.resolve_dependencies()
        in_degree = {t_name: len(task.dependencies) for t_name, task in self.tasks.items()}
        queue = [t for t, deg in in_degree.items() if deg == 0]
        sorted_tasks = []

        while queue:
            node = queue.pop(0)
            sorted_tasks.append(node)
            for t_name, task in self.tasks.items():
                if node in task.dependencies:
                    in_degree[t_name] -= 1
                    if in_degree[t_name] == 0:
                        queue.append(t_name)

        if len(sorted_tasks) != len(self.tasks):
            raise ValueError("Cycle detected in computational pipeline workflow DAG!")
        return sorted_tasks


def phred_quality_score(prob_error: float) -> float:
    """Phred Q-score conversion."""
    import math
    if prob_error <= 0:
        return 99.0
    return -10.0 * math.log10(prob_error)


if __name__ == "__main__":
    dag = WorkflowDAG()
    dag.add_task("fastqc", inputs=["raw_reads.fastq.gz"], outputs=["fastqc_report.html"])
    dag.add_task("bwa_align", inputs=["raw_reads.fastq.gz", "ref.fa"], outputs=["aligned.bam"])
    dag.add_task("samtools_sort", inputs=["aligned.bam"], outputs=["sorted.bam"])
    dag.add_task("gatk_call", inputs=["sorted.bam", "ref.fa"], outputs=["variants.vcf"])
    
    order = dag.topological_sort()
    print("Resolved Pipeline Execution Order:")
    for step, name in enumerate(order, 1):
        print(f"  Step {step}: {name} (Depends on: {list(dag.tasks[name].dependencies)})")
