# unschema

Convert KML with SchemaData to plain KML with Data/value. Primarily for converting KML exported from QGIS to schema-less format for compatibility when needed.

## What it does

Unschema transforms KML files by:
- Removing `<Schema>` definition blocks
- Converting `<SchemaData>` elements with `<SimpleData>` children into standard KML `<Data>` elements with `<value>` children
- Preserving all attribute data while making the KML compatible with applications that don't support schema-based extended data

## Installation

### Recommended: Install with pipx

```bash
pipx install git+https://github.com/OpticalFlyer/unschema.git
```

### Alternative: Install with pip

```bash
pip install git+https://github.com/OpticalFlyer/unschema.git
```

### Development installation

```bash
git clone https://github.com/OpticalFlyer/unschema.git
cd unschema
pip install -e .
```

## Usage

```bash
unschema input.kml output.kml
```

### Example

```bash
unschema qgis_export.kml compatible_output.kml
```

## Input/Output Example

**Input (QGIS schema-based KML):**
```xml
<Schema name="pole" id="pole">
  <SimpleField name="UUID" type="string"></SimpleField>
  <SimpleField name="Pole Tag" type="string"></SimpleField>
</Schema>
...
<ExtendedData>
  <SchemaData schemaUrl="#pole">
    <SimpleData name="UUID">fb660b34-8eb3-41ab-956b-ca37f36cd3bc</SimpleData>
    <SimpleData name="Pole Tag">s1983552_3202906-8446</SimpleData>
  </SchemaData>
</ExtendedData>
```

**Output (compatible KML):**
```xml
<ExtendedData>
  <Data name="UUID"><value>fb660b34-8eb3-41ab-956b-ca37f36cd3bc</value></Data>
  <Data name="Pole Tag"><value>s1983552_3202906-8446</value></Data>
</ExtendedData>
```

## Requirements

- Python 3.6+
- No external dependencies (uses only Python standard library)

## Why use this?

Some applications and web services don't properly handle KML files with schema-based extended data, particularly those exported from QGIS. This tool converts them to the more widely supported standard format while preserving all your attribute data.