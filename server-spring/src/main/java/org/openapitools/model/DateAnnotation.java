package org.openapitools.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.time.OffsetDateTime;
import org.openapitools.model.Annotation;
import org.openapitools.model.DateAnnotationAllOf;
import org.openapitools.model.User;
import org.openapitools.jackson.nullable.JsonNullable;
import javax.validation.Valid;
import javax.validation.constraints.*;

/**
 * A date annotation in a text
 */
@ApiModel(description = "A date annotation in a text")
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2020-10-21T10:20:06.779899-07:00[America/Los_Angeles]")

public class DateAnnotation   {
  @JsonProperty("id")
  private Integer id;

  @JsonProperty("createdBy")
  private User createdBy;

  @JsonProperty("createdAt")
  @org.springframework.format.annotation.DateTimeFormat(iso = org.springframework.format.annotation.DateTimeFormat.ISO.DATE_TIME)
  private OffsetDateTime createdAt;

  @JsonProperty("updatedBy")
  private User updatedBy;

  @JsonProperty("updatedAt")
  @org.springframework.format.annotation.DateTimeFormat(iso = org.springframework.format.annotation.DateTimeFormat.ISO.DATE_TIME)
  private OffsetDateTime updatedAt;

  @JsonProperty("noteId")
  private Integer noteId;

  @JsonProperty("start")
  private Integer start;

  @JsonProperty("length")
  private Integer length;

  @JsonProperty("text")
  private String text;

  @JsonProperty("format")
  private String format;

  public DateAnnotation id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * ID
   * @return id
  */
  @ApiModelProperty(example = "0", value = "ID")


  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }

  public DateAnnotation createdBy(User createdBy) {
    this.createdBy = createdBy;
    return this;
  }

  /**
   * Get createdBy
   * @return createdBy
  */
  @ApiModelProperty(value = "")

  @Valid

  public User getCreatedBy() {
    return createdBy;
  }

  public void setCreatedBy(User createdBy) {
    this.createdBy = createdBy;
  }

  public DateAnnotation createdAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * When the entity has been created
   * @return createdAt
  */
  @ApiModelProperty(value = "When the entity has been created")

  @Valid

  public OffsetDateTime getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
  }

  public DateAnnotation updatedBy(User updatedBy) {
    this.updatedBy = updatedBy;
    return this;
  }

  /**
   * Get updatedBy
   * @return updatedBy
  */
  @ApiModelProperty(value = "")

  @Valid

  public User getUpdatedBy() {
    return updatedBy;
  }

  public void setUpdatedBy(User updatedBy) {
    this.updatedBy = updatedBy;
  }

  public DateAnnotation updatedAt(OffsetDateTime updatedAt) {
    this.updatedAt = updatedAt;
    return this;
  }

  /**
   * When the entity has been updated
   * @return updatedAt
  */
  @ApiModelProperty(value = "When the entity has been updated")

  @Valid

  public OffsetDateTime getUpdatedAt() {
    return updatedAt;
  }

  public void setUpdatedAt(OffsetDateTime updatedAt) {
    this.updatedAt = updatedAt;
  }

  public DateAnnotation noteId(Integer noteId) {
    this.noteId = noteId;
    return this;
  }

  /**
   * The note ID
   * @return noteId
  */
  @ApiModelProperty(value = "The note ID")


  public Integer getNoteId() {
    return noteId;
  }

  public void setNoteId(Integer noteId) {
    this.noteId = noteId;
  }

  public DateAnnotation start(Integer start) {
    this.start = start;
    return this;
  }

  /**
   * The position of the first character
   * @return start
  */
  @ApiModelProperty(value = "The position of the first character")


  public Integer getStart() {
    return start;
  }

  public void setStart(Integer start) {
    this.start = start;
  }

  public DateAnnotation length(Integer length) {
    this.length = length;
    return this;
  }

  /**
   * The length of the annotation
   * @return length
  */
  @ApiModelProperty(value = "The length of the annotation")


  public Integer getLength() {
    return length;
  }

  public void setLength(Integer length) {
    this.length = length;
  }

  public DateAnnotation text(String text) {
    this.text = text;
    return this;
  }

  /**
   * The string annotated
   * @return text
  */
  @ApiModelProperty(value = "The string annotated")


  public String getText() {
    return text;
  }

  public void setText(String text) {
    this.text = text;
  }

  public DateAnnotation format(String format) {
    this.format = format;
    return this;
  }

  /**
   * Date format (ISO 8601)
   * @return format
  */
  @ApiModelProperty(value = "Date format (ISO 8601)")


  public String getFormat() {
    return format;
  }

  public void setFormat(String format) {
    this.format = format;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DateAnnotation dateAnnotation = (DateAnnotation) o;
    return Objects.equals(this.id, dateAnnotation.id) &&
        Objects.equals(this.createdBy, dateAnnotation.createdBy) &&
        Objects.equals(this.createdAt, dateAnnotation.createdAt) &&
        Objects.equals(this.updatedBy, dateAnnotation.updatedBy) &&
        Objects.equals(this.updatedAt, dateAnnotation.updatedAt) &&
        Objects.equals(this.noteId, dateAnnotation.noteId) &&
        Objects.equals(this.start, dateAnnotation.start) &&
        Objects.equals(this.length, dateAnnotation.length) &&
        Objects.equals(this.text, dateAnnotation.text) &&
        Objects.equals(this.format, dateAnnotation.format);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, createdBy, createdAt, updatedBy, updatedAt, noteId, start, length, text, format);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DateAnnotation {\n");
    
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    createdBy: ").append(toIndentedString(createdBy)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    updatedBy: ").append(toIndentedString(updatedBy)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    noteId: ").append(toIndentedString(noteId)).append("\n");
    sb.append("    start: ").append(toIndentedString(start)).append("\n");
    sb.append("    length: ").append(toIndentedString(length)).append("\n");
    sb.append("    text: ").append(toIndentedString(text)).append("\n");
    sb.append("    format: ").append(toIndentedString(format)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }
}

