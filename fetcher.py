

import os
from kubernetes import client, config

def main():

   node_name = os.environ['NODE_NAME']
   src_file_path = os.environ['SRC_FILE_PATH']
   dst_file_path = os.environ['DST_FILE_PATH']
   
   config..load_incluster_config()

   v1 = client.CoreV1Api()

   ret = v1.read_node(node_name)

   if not "failure-domain.beta.kubernetes.io/zone" in ret.metadata.labels.keys():
      print("Missing \"failure-domain.beta.kubernetes.io/zone\" label.")
      exit(1)

   zone = et.metadata.labels["failure-domain.beta.kubernetes.io/zone"]

   with open(src_file_path, 'r') as src:
      src_content = src.read()

   dst_content = src_content.replace("${ZONE}", zone)

   with open(dst_file_path, 'w') as dst:
      dst.write(dst_content)

   print("Replaced label")

if __name__ == '__main__':
   main()
