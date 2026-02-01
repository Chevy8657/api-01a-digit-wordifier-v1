# Digit Wordifier

Single-purpose API. Stateless. Deterministic. Returns JSON only.

## Endpoints
- GET `/health`
- GET `/v1/digit-wordify?text=`

## Example

Request:
`/v1/digit-wordify?text=12345`

Response:
```json
{
  "input": "12345",
  "wordified": "one two three four five"
}
