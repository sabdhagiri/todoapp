terraform {
    required_providers {
        google = {
            source = "hashicorp/google"
        }
    }
}

provider "google" {
    version = "3.5.0"

    project = "sg-labs"
    region = "us-west1"
    zone = "us-west1-a"
}

resource "google_container_cluster" "primary" {
    name = "dev-cluster"
    location = "us-west1-a"
    initial_node_count = 1
    logging_service = "logging.googleapis.com/kubernetes"
    monitoring_service = "monitoring.googleapis.com/kubernetes"
}

output "dev-cluster-name" {
    value = google_container_cluster.primary.name
}

resource "google_compute_address" "todoapp_lb_ip" {
    name = "todoapp-lb-ip"
}

output "todoapp_lb_ip" {
    value = google_compute_address.todoapp_lb_ip.address
}