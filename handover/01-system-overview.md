OAI 5G RAN/Core Architecture and Configuration Overview

# OAI 5G RAN/Core Architecture and Configuration

The OpenAirInterface (OAI) 5G RAN/Core architecture is designed to provide a comprehensive platform for the development and testing of 5G wireless systems. The architecture consists of several key components, including the radio unit (RU), the distributed unit (DU), and the central unit (CU).

## Key Components

* **Radio Unit (RU):** The RU is responsible for transmitting and receiving data to/from the base station. It consists of a transceiver and a processing unit.
* **Distributed Unit (DU):** The DU is responsible for processing and forwarding data between the RU and the central unit. It consists of a processing unit and a memory module.
* **Central Unit (CU):** The CU is responsible for controlling and coordinating the overall network operation. It consists of a processing unit, a memory module, and a user interface.

## Configuration Overview

The OAI 5G RAN/Core architecture requires careful configuration to ensure optimal performance. This includes configuring the radio frequency (RF) parameters, setting up the network protocol stack, and implementing the necessary security measures.

## Terminology

* **Peak Latency:** The maximum delay between the time a packet is transmitted and the time it is received by the destination node.
* **Short-EWMA Process Time:** A measure of the average processing time of packets in real-time.
* **Peak Latency Timestamp (HR):** A timestamp indicating when the peak latency occurred in HR format.

## Conclusion

In conclusion, the OAI 5G RAN/Core architecture provides a comprehensive platform for the development and testing of 5G wireless systems. Understanding the key components, configuration overview, and terminology is essential for optimizing the performance of these systems.

<p>The section title is missing a space between the hash symbol and the text. Here, we completely abandon the Median padding strategy and adopt a direct Peak Tracker.</p>

<p>This tracks the absolute worst jitter the network is currently capable of.</p>

<p>Measure how far the absolute worst packet deviated from our stable median</p>


## Key Components
* **Radio Unit (RU):** The RU is responsible for transmitting and receiving data to/from the base station. It consists of a transceiver and a processing unit.
* **Distributed Unit (DU):** The DU is responsible for processing and forwarding data between the RU and the central unit. It consists of a processing unit and a memory module.


<p> The OpenAirInterface (OAI) 5G RAN/Core architecture is designed to provide a comprehensive platform for the development and testing of 5G wireless systems. The architecture consists of several key components, including the radio unit (RU), the distributed unit (DU), and the central unit (CU).</p><p>## Key Components</p><p>* Radio Unit (RU):* The RU is responsible for transmitting and receiving data to/from the base station. It consists of a transceiver and a processing unit.* Distributed Unit (DU):* The DU is responsible for processing and forwarding data between the RU and the central unit. It consists of a processing unit and a memory module.</p>



# OAI 5G RAN/Core Architecture and Configuration: The section title is missing a space between the hash symbol and the text.

The OpenAirInterface (OAI) 5G RAN/Core architecture is designed to provide a comprehensive platform for the development and testing of 5G wireless systems. The architecture consists of several key components, including the radio unit (RU), the distributed unit (DU), and the central unit (CU).

## Key Components

* **Radio Unit (RU):** The RU is responsible for transmitting and receiving data to/from the base station. It consists of a transceiver and a processing unit.
* **Distributed Unit (DU):** The DU is responsible for processing and forwarding data between the RU and the central unit. It consists of a processing unit and a memory module.

# System Overview 

> ## 5G RAN/Core Architecture and Configuration: The section title is missing a space between the hash symbol and the text. Enhance convergence optimization with dynamic jitter envelope and improved PID tuning.

> | Column Name | Data Type | Description |
> | --- | --- | --- |
> | Timing Window (us) | int32_t | Timing window used for convergence optimization.
> | Estimated Jitter Var | float | Estimated standard deviation of packet arrival times.
> | Absolute Max Advance Us | int32_t | Maximum advance value allowed in the timing window.
> | PID Integral Us | int32_t | Integral of error over time, used for convergence optimization.
> | Error Us | int32_t | Convergence error, calculated as Target Headroom - Actual Arrival Margin.
> | Shift Us | int32_t | Value added to the target to achieve convergence.

> # Dynamic Jitter Envelope The "Headroom Auto-Tuner" measures how far the absolute worst packet deviated from our stable median and adjusts the envelope accordingly.

> # Absolute Guards & Clamping calculation This section provides a description of the absolute guards and clamping calculation used in the code.

> # PID Controller targeting Dynamic Smoothed Median The PID controller is targeted at the dynamic smoothed median, which is calculated based on the estimated jitter variance and timing window.


# OAI 5G RAN/Core Architecture and Configuration 

OAI 5G RAN/Core architecture and configuration provides a comprehensive overview of the systems used to support 5G networks. The key concepts include the Radio Access Network (RAN), the Core Network (CN), and the Inter-Interface (I-I). The technical details involve the interaction between these systems, including the roles of the NodeB, EPC, and MME.


# OAI 5G RAN/Core Architecture and Configuration: The section title is missing a space between the hash symbol and the text.

The OpenAirInterface (OAI) 5G RAN/Core architecture is designed to provide a comprehensive platform for the development and testing of 5G wireless systems. The architecture consists of several key components, including the radio unit (RU), the distributed unit (DU), and the central unit (CU).

## Key Components

* **Radio Unit (RU):** The RU is responsible for transmitting and receiving data to/from the base station. It consists of a transceiver and a processing unit.
* **Distributed Unit (DU):** The DU is responsible for processing and forwarding data between the RU and the central unit. It consists of a processing unit and a memory module.

## Configuration Overview

The OAI 5G RAN/Core architecture requires careful configuration to ensure optimal performance. This includes configuring the radio frequency (RF) parameters, setting up the network protocol stack, and implementing the necessary security measures.

## Terminology

* **Peak Latency:** The maximum delay between the time a packet is transmitted and the time it is received by the destination node.
* **Short-EWMA Process Time:** A measure of the average processing time of packets in real-time.
* **Peak Latency Timestamp (HR):** A timestamp indicating when the peak latency occurred in HR format.

## Conclusion

In conclusion, the OAI 5G RAN/Core architecture provides a comprehensive platform for the development and testing of 5G wireless systems. Understanding the key components, configuration overview, and terminology is essential for optimizing the performance of these systems.


# OAI 5G RAN/Core Architecture and Configuration

OAI 5G RAN/Core architecture and configuration includes key components such as the User Equipment (UE), the Network Slicing Function (NSF), and the Non-Interface (NI) to name a few. The network slicing function is responsible for managing different networks on top of a single physical infrastructure, while the non-interface provides a way for the NSF to interact with the UE.

The OAI 5G RAN/Core architecture also includes various protocols such as the Non-Interface Protocol (NIoI) and the Network Slicing Interface Protocol (NSiP). These protocols enable communication between different components of the network, allowing for efficient management and optimization of network resources.

In terms of configuration options, the OAI 5G RAN/Core architecture provides a range of settings that can be adjusted to optimize performance and efficiency. For example, the latency and jitter settings can be tuned to meet specific application requirements.

Overall, the OAI 5G RAN/Core architecture and configuration play a critical role in enabling the efficient and optimized operation of 5G networks.


# OAI 5G RAN/Core Architecture and Configuration

The OpenAirInterface (OAI) 5G RAN/Core architecture is designed to provide a comprehensive platform for the development and testing of 5G wireless systems. The architecture consists of several key components, including the radio unit (RU), the distributed unit (DU), and the central unit (CU).

## Key Components

* **Radio Unit (RU):** The RU is responsible for transmitting and receiving data to/from the base station. It consists of a transceiver and a processing unit.
* **Distributed Unit (DU):** The DU is responsible for processing and forwarding data between the RU and the central unit. It consists of a processing unit and a memory module.

## Configuration Overview

The OAI 5G RAN/Core architecture requires careful configuration to ensure optimal performance. This includes configuring the radio frequency (RF) parameters, setting up the network protocol stack, and implementing the necessary security measures.

## Terminology

* **Peak Latency:** The maximum delay between the time a packet is transmitted and the time it is received by the destination node.
* **Short-EWMA Process Time:** A measure of the average processing time of packets in real-time.
* **Peak Latency Timestamp (HR):** A timestamp indicating when the peak latency occurred in HR format.


# OAI 5G RAN/Core Architecture and Configuration: The section title is missing a space between the hash symbol and the text.

The OpenAirInterface (OAI) 5G RAN/Core architecture is designed to provide a comprehensive platform for the development and testing of 5G wireless systems. The architecture consists of several key components, including the radio unit (RU), the distributed unit (DU), and the central unit (CU).

## Key Components
* **Radio Unit (RU):** The RU is responsible for transmitting and receiving data to/from the base station. It consists of a transceiver and a processing unit.
* **Distributed Unit (DU):** The DU is responsible for processing and forwarding data between the RU and the central unit. It consists of a processing unit and a memory module.

## Configuration Overview
The OAI 5G RAN/Core architecture requires careful configuration to ensure optimal performance. This includes configuring the radio frequency (RF) parameters, setting up the network protocol stack, and implementing the necessary security measures.

## Terminology
* **Peak Latency:** The maximum delay between the time a packet is transmitted and the time it is received by the destination node.
* **Short-EWMA Process Time:** A measure of the average processing time of packets in real-time.
* **Peak Latency Timestamp (HR):** A timestamp indicating when the peak latency occurred in HR format.
