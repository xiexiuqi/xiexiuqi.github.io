# 服务器处理器规格表 - 补充说明

## ⚠️ 重要声明

**本页面所有内容均由 AI 生成，基于公开资料整理。**

- 包含已发布和预发布产品信息
- 预发布产品规格可能存在变动，请以官方最终发布为准
- 部分数据来自技术媒体报道（AnandTech, Tom's Hardware 等）
- 如有错误，欢迎指正

## 预发布产品说明

标注 `*` 或带有 **预发布** 标签的产品为尚未正式发布的产品，其规格基于：
- 官方路线图
- 技术媒体爆料
- 行业分析师预测

### Intel 预发布产品

#### 7th Gen Xeon (Clearwater Forest)
- **架构**: Lion Cove 性能核 + Skymont 能效核
- **制程**: Intel 18A (1.8nm 级)
- **预计发布**: 2025 Q4
- **来源**: Intel 官方路线图, AnandTech, Tom's Hardware

**主要型号**:
- Xeon 7980V: 144核/288线程, 576MB L3, 500W TDP
- Xeon 7960V: 96核/192线程, 384MB L3, 400W TDP

### AMD 预发布产品

#### EPYC 10000 系列 (Zen 6 / Medusa)
- **架构**: Zen 6
- **制程**: TSMC 3nm
- **预计发布**: 2025 Q4 - 2026 Q1
- **来源**: AMD 官方路线图, AdoredTV, Moore's Law Is Dead

**主要型号**:
- EPYC 10965: 256核/512线程, 1024MB L3, 500W TDP
- EPYC 10775: 192核/384线程, 768MB L3, 450W TDP

### Arm 预发布产品

#### Arm AGI CPU
- **架构**: Arm Neoverse V3
- **制程**: TSMC 3nm
- **预计发布**: 2026 Q2
- **来源**: Arm 官方, ServeTheHome

**主要规格**:
- 核心数: 最多 136 核心 (单路)
- L2 缓存: 每核心 2MB (共 272MB)
- 内存: 12 通道 DDR5-8800
- PCIe: 96 条 PCIe Gen6 通道，支持 CXL
- 设计: 双芯片设计
- 发布时间: 2026 年 3 月 24 日宣布，预计 2026 年晚些时候量产
- 目标市场: AI 数据中心、代理式 AI 工作负载
- 主要客户: Meta、OpenAI、Cloudflare、SAP
- 系统合作伙伴: Lenovo、ASRock Rack、QCT、Supermicro

### 国产处理器预发布产品

#### 华为鲲鹏
- **鲲鹏 930**: 预计 2025 年发布，ARMv9 架构，5nm 制程
- **来源**: 华为官方路线图, 产业链消息

#### 海光
- **海光 8 系**: 预计 2025 年发布，支持 DDR5
- **来源**: 海光官方路线图

#### 飞腾
- **腾云 S6000**: 预计 2025 年发布，ARMv9 架构
- **来源**: 飞腾官方路线图

#### 龙芯
- **3A6000 服务器版**: 预计 2025 年发布
- **3E7000**: 预计 2026 年发布，支持多路互联
- **来源**: 龙芯官方路线图

#### 兆芯
- **KH-50000 系列**: 预计 2025 年发布，支持 DDR5
- **来源**: 兆芯官方路线图

## 内存带宽计算方法

内存带宽 = 内存频率 × 内存通道数 × 64bit / 8

示例：
- DDR5-6400, 12通道: 6400 × 12 × 8 = 614.4 GB/s
- DDR5-4800, 8通道: 4800 × 8 × 8 = 307.2 GB/s

## 核存比说明

核存比 = 内存带宽 / 核心数

表示每个核心可分配的内存带宽，数值越高越好。

## 数据来源

### 官方来源
- Intel ARK: https://ark.intel.com
- AMD 官方: https://www.amd.com/en/processors/epyc
- 华为鲲鹏: https://www.hikunpeng.com
- 海光: http://www.hygon.cn
- 飞腾: https://www.phytium.com.cn
- 龙芯: http://www.loongson.cn
- 兆芯: http://www.zhaoxin.com
- AWS: https://aws.amazon.com/ec2/graviton
- Ampere: https://amperecomputing.com
- Arm: https://www.arm.com/products/cloud-datacenter/arm-agi-cpu

### 技术媒体
- AnandTech: https://www.anandtech.com
- Tom's Hardware: https://www.tomshardware.com
- ServeTheHome: https://www.servethehome.com
- WikiChip: https://en.wikichip.org

## 更新日志

- **2025-03-04**: 初始版本，包含 9 大厂商处理器规格
- **2025-03-04**: 添加预发布产品（Intel Clearwater Forest, AMD Zen 6）
- **2025-03-04**: 添加内存带宽和核存比列
- **2025-03-04**: 添加 AI 生成声明和数据来源标注
- **2025-04-01**: 添加 Arm AGI CPU（预发布产品）

## 注意事项

1. **预发布产品规格可能变动**: 请以官方最终发布为准
2. **国产处理器数据**: 部分数据来自公开资料，可能不完整
3. **AI 生成内容**: 本页面由 AI 辅助生成，已尽量确保准确性
4. **持续更新**: 会随着产品发布持续更新

---

**最后更新**: 2025年4月1日  
**生成工具**: AI Assistant  
**数据来源**: 公开资料整理
